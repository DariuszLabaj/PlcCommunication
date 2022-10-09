from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ErrorLogClear() -> bytes:
    """
    Clears all error log records
    """
    return CmdBytes.ErrorLogClear.to_bytes()
