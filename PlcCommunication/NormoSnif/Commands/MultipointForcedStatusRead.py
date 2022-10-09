from PlcCommunication.NormoSnif.IFrame import IFrame
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def MultipointForcedStatusRead(
    areaCode: IFrame.MemAreaDesignation, beginningAddress: int, noOfUnits: int
) -> bytes:
    """
    Reads the forced status of the specified range of words or timers/counters.\n
    Memory area code, Beginning address, Number of units (command, response): Specify the memory area code, the
    beginning address in that area, and the number of words or timers/counters to read. The number of units can be
    between 0001 and 0040 (1 to 64 in decimal). The actual area, beginning address, and number of unit to be read
    will be returned in the response.\n
    Memory Areas Forced status can be read in the following areas. Refer to Memory Area Designations for memory area
    designations.\n
    Data (response): Forced status is returned beginning from the specified word or timer/counter. The number of
    bytes returned will be (the number of units) x (the number of bytes/unit).
    """
    if beginningAddress > 0xFFFF:
        raise ValueError("Begining address must be 2 byte word (less then 0xFFFF)")
    if noOfUnits == 0 or noOfUnits > 64:
        raise ValueError(
            "The number of units must be between 0001 and 0040 (1 to 64 in decimal)"
        )
    commandData = CmdBytes.MulPointForceStatusRead.to_bytes()
    commandData += areaCode.to_bytes()
    commandData += beginningAddress.to_bytes(2, "big")
    commandData += b"\x00"
    commandData += noOfUnits.to_bytes(2, "big")
    return commandData
