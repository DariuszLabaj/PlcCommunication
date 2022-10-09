from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def NameDelete() -> bytes:
    """
    Deletes the name of a SYSMAC NET Link Unit.
    """
    return CmdBytes.NameDel.to_bytes()
