from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ParameterAreaClear(
    areaCode: IFrame.MemAreaDesignation, beginningWord: int, noOfWords: int
) -> bytes:
    """
    Writes all zeros to the specified number of consecutive parameter area words to clear the previous data. The I/O
    table can be cleared only when the PC is in PROGRAM mode. Always clear the entire range of the specified
    parameter area.\n
    Parameter area code (command): The parameter area to clear.\n
    Beginning word (command): Fixed at 0000.\n
    No. of words (command): The number of words to clear (see diagram below).\n
    Data (command): Set to 0000. The number of word addresses where the data (0000) should be written is specified
    by the number of words in the command block.\n
    Parameters Areas - The available parameter areas and the number of words in each are as shown below. The number
    of words in the parentheses is specified as the number of words to clear.\n
    0x80 0x00 0000 to 0FFF\n
    0x80 0x10 0000 to 00FF - PC setup\n
    0x80 0x01 0000 to 06BF\n
    0x80 0x11 0000 to 00BF - Peripheral Device settings\n
    0x80 0x12 0000 to 03FF - I/O table\n
    0x80 0x13 0000 to 01FF - Routing tables\n
    0x80 0x02 0000 to 083F - CPU Bus Unit settings
    """
    if len(areaCode) != 2:
        raise ValueError("areaCode - must contain 2 parameter area bytes")
    if areaCode[0] != 0x80:
        raise ValueError("areaCode - first byte of parameter area code must be 0x80")
    if noOfWords < 1:
        raise ValueError("noOfWords - must be grather then 0")
    commandData = CmdBytes.ParamAreaClear.to_bytes()  # Set command bytes
    commandData += areaCode.to_bytes()  # Set memory area code
    commandData += beginningWord.to_bytes(2, "big")
    commandData += noOfWords.to_bytes(2, "big")  # Set Number of items to write
    commandData += b'\x00\x00'
    return commandData
