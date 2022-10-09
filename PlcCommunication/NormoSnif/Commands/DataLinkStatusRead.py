from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def DataLinkStatusRead() -> bytes:
    """
    Reads the data link status of the SYSMAC NET Link
    """
    return CmdBytes.DLinkStatRead.to_bytes()
