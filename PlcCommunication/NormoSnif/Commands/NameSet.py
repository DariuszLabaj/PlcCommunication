from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def NameSet(nameData: str) -> bytes:
    """
    Registers a name for the SYSMAC NET Link Unit.\n
    Name data (command): The data set must be within 8 bytes in ASCII. Do not use the NULL (00) code.
    """
    if len(nameData) < 8:
        for _ in range(8 - len(nameData)):
            nameData += " "
    nameData = bytes(nameData[:8], "ascii")
    commandData = CmdBytes.NameSet.to_bytes()
    commandData += nameData
    return commandData
