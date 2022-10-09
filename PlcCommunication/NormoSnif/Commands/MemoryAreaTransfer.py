from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes
from typing import List


def MemoryAreaTransfer(
    areaCodes: List[IFrame.MemAreaDesignation],
    beginningAddress: List[int],
    noOfItems: int,
) -> bytes:
    """
    Copies and transfers the contents of the specified number of consecutive memory area words to the specified
    memory area. All source words must be in MEMORY AREA TRANSFER Section the same area and all designation words
    must be written to the same area (here, all memory areas with the same memory area code are considered as
    one area).\n
    Memory area code (command): The data area to transfer from and the data area to transfer to.\n
    Beginning address (command): The first word/value to transfer from and the first word to transfer to.\n
    No. of items (command): The number of items to transfer (each item consists of two bytes).
    """
    if len(areaCodes) != 2:
        raise ValueError("areaCode - must contain 2 memory area codes")
    if len(beginningAddress) != 2:
        raise ValueError("beginningAddress - must contain 2 addresses")
    if noOfItems < 1:
        raise ValueError("noOfItems - must be grather then 0")
    commandData = CmdBytes.MemAreaTran.to_bytes()  # Set command bytes
    for i, areaCode in enumerate(areaCodes):
        commandData += areaCode.to_bytes()
        commandData += beginningAddress[i].to_bytes(2, "big")
        commandData += b"\x00"  # Select byte or word type
    commandData += noOfItems.to_bytes(2, "big")  # Set Number of items to write
    return commandData
