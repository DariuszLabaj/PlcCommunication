from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def AccessRightForcedAquire() -> bytes:
    """
    Acquires the access right even if another device already holds it.
    """
    commandData = CmdBytes.AccessRightFAq.to_bytes()
    commandData += b"\x00\x00"
    return commandData
