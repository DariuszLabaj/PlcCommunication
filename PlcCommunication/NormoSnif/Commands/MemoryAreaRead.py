from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def MemoryAreaRead(
    areaCode: IFrame.MemAreaDesignation, beginningAddress: int, noOfItems: int
) -> bytes:
    """
    Reads the contents of the specified number of consecutive memory area words
    starting from the specified word. All words must be in the same memory area
    (here, all memory areas with the same memory area code are considered as one area).\n
    Memory area code (command): The data area to read. CIO, WR, HR, DM\n
    Beginning address (command): The address of the first word/bit/flag to read from memory.\n
    No. of items (command): The number of items to be read.\n
    Data (response): The data from the specified words is returned in sequence
    starting from the beginning address. The required number of bytes in total is calculated as follows:\n
        No. of bytes required by each item x No. of items\n
    word_bit -- Specify the the bit between 00 and 0F (00 to 15).\n
        Set to 00 to specify channel or flag data.
    """
    if noOfItems < 1:
        raise ValueError("noOfItems - must be greather then 0")
    commandData = CmdBytes.MemAreaRead.to_bytes()  # Set command bytes
    commandData += areaCode.to_bytes()  # Set memory area code
    commandData += beginningAddress.to_bytes(2, "big")  # Set beginning address
    commandData += b"\x00"  # Select byte or word type
    commandData += noOfItems.to_bytes(2, "big")  # Set Number of items to read
    return commandData
