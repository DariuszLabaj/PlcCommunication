from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ProgramAreaProtect(password: bytearray) -> bytes:
    """
    Protects the program by removing all read/write access rights.\n
    The command will be executed normally even if the beginning word and last word are set to values other than
    those shown below.\n
    Program no. (command): Set to 0000.\n
    Protect code (command): Set to 00.\n
    Beginning word (command): Set to 00000000\n
    Last word (command): Set to FFFFFFFF\n
    Password (command): Set any four ASCII characters. The password is used with the PROGRAM AREA PROTECT CLEAR
    command
    """
    if len(password) != 4:
        raise ValueError("password must contain 4 bytes")
    commandData = CmdBytes.ProgAreaProtect.to_bytes()
    commandData += bytes(
        bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF])
    )
    commandData += bytes(password)
    return commandData
