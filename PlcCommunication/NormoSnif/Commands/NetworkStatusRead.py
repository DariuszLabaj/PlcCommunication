from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def NetworkStatusRead() -> bytes:
    """
    Reads the status of the SYSMAC LINK Network.
    """
    return CmdBytes.NetStatRead.to_bytes()
