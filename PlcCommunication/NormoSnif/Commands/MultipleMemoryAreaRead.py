from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes
from typing import List


def MultipleMemoryAreaRead(
    areaCodes: List[IFrame.MemAreaDesignation], beginningAddress: List[int]
) -> bytes:
    """
    Reads the contents of the specified number of non-consecutive memory area
    words, starting from the specified word.\n
    Memory area code (command): The data area to read.\n
    Address (command): The word/bit/flag to read. The content of up to 128 address
    can be read.
    """
    commandData = CmdBytes.MulMemAreaRead.to_bytes()  # Set command bytes
    for i, areaCode in enumerate(areaCodes):
        commandData += areaCode.to_bytes()
        commandData += beginningAddress[i].to_bytes(2, "big")
        commandData += b"\x00"  # Select byte or word type
    return commandData
