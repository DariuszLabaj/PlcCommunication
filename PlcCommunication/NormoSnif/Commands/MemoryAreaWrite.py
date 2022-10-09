from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def MemoryAreaWrite(
    areaCode: IFrame.MemAreaDesignation,
    beginningAddress: int,
    dataAray: bytearray,
) -> bytes:
    """
    Writes data to the specified number of consecutive words starting from the specified word. All words must be in
    the same memory area (here, all memory areas
    with the same memory area code are considered as one area).\n
    Memory area code (command): The data area to write. CIO, DM\n
    Beginning address (command): The first word/value to write.\n
    No. of items (command): The number of items to be written. Set the number of items to 0001 when writing a step
    timer PV, register value, or interrupt status.\n
    Data (command): The data to be written. The required number of bytes in total is calculated as follows:\n
        No. of bytes required by each item x No. of items
    """
    noOfItems = int(dataAray / 2)
    commandData = CmdBytes.MemAreaWrite.to_bytes()  # Set command bytes
    commandData += areaCode.to_bytes()  # Set memory area code
    commandData += beginningAddress.to_bytes(2, "big")  # Set beginning address
    commandData += b"\x00"  # Select byte or word type
    commandData += noOfItems.to_bytes(2, "big")  # Set Number of items to write
    for byte in dataAray:
        commandData += byte
    return commandData
