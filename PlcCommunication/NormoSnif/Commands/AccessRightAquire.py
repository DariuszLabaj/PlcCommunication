from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def AccessRightAquire() -> bytes:
    """
    Acquires the access right as long as no other device holds it. Execute the ACCESS RIGHT ACQUIRE command when you
    need to execute commands continuously without being interrupted by other devices. As soon as the execution of
    the commands has been completed, execute the ACCESS RIGHT RELEASE command to release the access right (refer to
    2-30 ACCESS RIGHT RELEASE). If another devices holds the access right, the device will be identified in the
    response.
    """
    commandData = CmdBytes.AccessRightAq.to_bytes()
    commandData += b"\x00\x00"
    return commandData
