from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def MemoryAreaFill(
    areaCode: IFrame.MemAreaDesignation,
    beginningAddress: int,
    noOfItems: int,
    data: int,
) -> bytes:
    """
    Writes the same data to the specified number of consecutive memory area words. All words must be in the same
    memory area (here, all memory areas with the same memory area code are considered as one area).\n
    Memory area code (command): The data area to write.\n
    Beginning address (command): The first word/values to write.\n
    No. of items (command): The number of items to write.\n
    Data (command): The data to be written to the memory area starting from the\n
    Beginning address. The data to be written should consist of two bytes. The following data can be written
    """
    if noOfItems < 1:
        raise ValueError("noOfItems - must be greather then 0")
    commandData = CmdBytes.MemAreaFill.to_bytes()  # Set command bytes
    commandData += areaCode.to_bytes()  # Set memory area code
    commandData += beginningAddress.to_bytes(2, "big")  # Set beginning address
    commandData += b"\x00"  # Select byte or word type
    commandData += noOfItems.to_bytes(2, "big")  # Set Number of items to write
    commandData += data.to_bytes(2, "big")
    return commandData
