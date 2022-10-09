from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def FalFalsRead(failNo: int) -> bytes:
    """
    Reads FAL/FALS messages\n
    FAL/FALS no. (command and response): In the command block, specify in hexadecimal in bits 0 to 13 the FAL or
    FALS number to be read as shown below. In the response block, the FAL or FALS number is returned.
    """
    if failNo > 0x3FFF:
        raise ValueError("Error code out of range")
    commandData = CmdBytes.MessageRead.to_bytes()
    commandData += (failNo + 0x8000).to_bytes(2, byteorder="big")
    return commandData
