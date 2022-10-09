from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def Reset() -> bytes:
    """
    Resets the SYSMAC NET Link Unit.
    """
    return CmdBytes.Reset.to_bytes()
