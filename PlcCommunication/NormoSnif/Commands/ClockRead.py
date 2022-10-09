from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ClockRead() -> bytes:
    """
    Reads the clock.\n
    Year, month, date, hour, minute, second, day (response): Each value is expressed in BCD.
    """
    return CmdBytes.ClockRead.to_bytes()
