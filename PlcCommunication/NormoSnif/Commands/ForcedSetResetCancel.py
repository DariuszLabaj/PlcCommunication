from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ForcedSetResetCancel() -> bytes:
    """
    Cancels all bits (flags) that have been forced ON or forced OFF
    """
    return CmdBytes.ForceSetResetCancel.to_bytes()
