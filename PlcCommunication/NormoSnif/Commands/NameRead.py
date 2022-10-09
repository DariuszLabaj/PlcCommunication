from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def NameRead() -> bytes:
    """
    Reads the name of a SYSMAC NET Link Unit.
    """
    return CmdBytes.NameRead.to_bytes()
