from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ParameterAreaRead(
    areaCode: IFrame.MemAreaDesignation, beginningWord: int, noOfWords: int
) -> bytes:
    """
    Reads the contents of the specified number of consecutive parameter area words starting from the specified word.
    All words in the specified parameter area must be read at the same time to ensure complete data. A maximum of
    266 words can be read with each command. To read larger parameter areas, use multiple commands and specify the
    beginning word and number of words for each.\n
    Parameter area code (command and response): The parameter area to read.\n
    Beginning word (command and response): The first word to read.\n
    No. of words (command and response): Bits 0 to 14 are used to specify the number of words to be read (each word
    consists of two bytes). Bit 15 must be OFF (0) in the command block. When the contents in the response block
    contains the last word of data in the specified parameter area, bit 15 will be ON (1).\n
    Data (response): The data in the specified parameter area will be returned in sequence starting from the
    beginning word. The leftmost bits (bits 8 to 15) of each word are read first, followed by the rightmost bits
    (bits 0 to 7). The required number of bytes in total for each read is calculated as follows:\n
    No. of words x 2 (each word consists of two bytes)\n
    Parameter Areas - There are five parameter areas, each of which has consecutive word addresses beginning from
    0000. The following data can be read. The word ranges in parentheses show the possible values for the beginning
    word.\n
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
    commandData = CmdBytes.ParmAreaRead.to_bytes()  # Set command bytes
    commandData += areaCode.to_bytes()  # Set memory area code
    commandData += beginningWord.to_bytes(2, "big")
    commandData += noOfWords.to_bytes(2, "big")  # Set Number of items to write
    return commandData
