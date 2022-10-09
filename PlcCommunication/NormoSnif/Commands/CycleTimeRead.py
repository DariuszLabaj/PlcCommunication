from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def CycleTimeRead() -> bytes:
    """
    Initializes the PC’s cycle time history or reads the average, max., and min. cycle time.\n
    Parameter code (command): As follows:\n
    00: Initializes the cycle time.\n
    01: Reads the average, maximum, and minimum cycle time.\n
    Average cycle time, max. cycle time, min. cycle time (response): Each value is expressed in 8-digit BCD in
    0.1-ms increments. For example, if 00 00 06 50 is returned, the cycle time is 65 ms.\n
    The average cycle time is obtained as follows:\n
    Average cycle time = (max. cycle time + min. cycle time)/2
    """
    commandData = CmdBytes.CTimeRead.to_bytes()
    commandData += b"\x00"
    return commandData
