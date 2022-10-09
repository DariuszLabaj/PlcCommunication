from typing import List
from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ParameterAreaWrite(
    areaCode: IFrame.MemAreaDesignation,
    beginningWord: int,
    noOfWords: int,
    data: List[int],
) -> bytes:
    """
    Writes data to the specified number of consecutive parameter area words starting from the specified word. All
    words in the specified parameter area must be written at the same time to ensure complete data. A maximum of 266
    words can be written with each command. To write larger parameter areas, use multiple commands and specify the
    beginning word for each. Data can be written to the I/O table only when the PC is in PROGRAM mode.\n
    Parameter area code (command): The parameter area to write.\n
    Beginning word (command): The first word to write.\n
    No. of words (command): Bits 0 to 14 are used to specify the number of words to be written (each word consists
    of two bytes). Bit 15 must be ON (1) when data is written to the last word in the specified parameter area or no
    data will be written. If the number of write words is set to 0000, no words will be written and a normal
    response code will be returned.\n
    Data (command): The data to be written. The leftmost bits (bits 15 to 8) of each word must be specified first,
    followed by the rightmost bits (bits 7 to 0). The required number of bytes in total for each write can be
    calculated as follows:\n
    No. of words x 2 (each word consists of two bytes)\n
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
    if areaCode.to_bytes()[0] != 0x80:
        raise ValueError("areaCode - first byte of parameter area code must be 0x80")
    if beginningWord < 0:
        raise ValueError("beginningWord - must be positive number")
    if noOfWords < 1:
        raise ValueError("noOfWords - must be grather then 0")
    if len(data) < noOfWords:
        raise ValueError("Amount of data is less then number of words to send")
    commandData = CmdBytes.ParmAreaWrite.to_bytes()  # Set command bytes
    commandData += areaCode.to_bytes()  # Set memory area code
    commandData += beginningWord.to_bytes(2, "big")
    commandData += noOfWords.to_bytes(2, "big")  # Set Number of items to write
    for i in range(noOfWords):
        commandData += data[i].to_bytes(2, "big")
    return commandData
