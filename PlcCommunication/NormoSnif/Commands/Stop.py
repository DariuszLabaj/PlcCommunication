from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def Stop() -> bytes:
    """
    Changes the PC to PROGRAM mode, stopping program execution.
    """
    return CmdBytes.Stop.to_bytes()
