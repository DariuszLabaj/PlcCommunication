from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ControllerStatusRead() -> bytes:
    """
    Reads the status of the Controller.
    """
    return CmdBytes.CtrStatRead.to_bytes()
