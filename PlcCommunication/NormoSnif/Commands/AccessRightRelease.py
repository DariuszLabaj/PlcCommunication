from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def AccessRightRelease() -> bytes:
    """
    Releases the access right regardless of what device holds it. A normal response code will returned even when
    another device held the access right or when no device held the access right.
    """
    commandData = CmdBytes.AccessRightRel.to_bytes() + b"\x00\x00"
    return commandData
