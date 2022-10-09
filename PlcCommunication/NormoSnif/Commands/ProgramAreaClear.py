from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ProgramAreaClear() -> bytes:
    """
    Clears the contents of the program area\n
    Program no. (command): Set to 0000.\n
    Clear code (command): Set to 00.
    """
    commandData = CmdBytes.ProgAreaClear.to_bytes()
    commandData += b"\x00\x00\x00"
    return commandData
