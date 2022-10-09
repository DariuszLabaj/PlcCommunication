from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ProgramAreaRead(beginningAddress: int, noOfBytes: int, programNo: int = 0) -> bytes:
    """
    Reads the contents of the specified number of consecutive program area words
    starting from the specified word. The program is read a machine language (object
    code). A maximum of 512 bytes can be read with each command.\n
    -- Program no. -- (command and response): Set to 0000.\n
    -- Beginning address -- (command and response): Set an relative byte address
    with 00000000 as the starting address. The beginning word must be an even
    number. The address set in the command will be returned in the response.\n
    -- No. of bytes -- (command and response): The number of bytes in an even number
    0200 (512 in decimal) or smaller. The number of bytes actually read will be
    returned in the response. Bit 15 will be ON (1) in the response block when the
    last word data of the program area is returned.
    """
    if noOfBytes < 1:
        raise ValueError("noOfBytes - must be grather then 0")
    commandData = CmdBytes.ProgAreaRead.to_bytes()
    commandData += programNo.to_bytes(2, "big")
    commandData += beginningAddress.to_bytes(4, "big")
    commandData += noOfBytes.to_bytes(2, "big")
    return commandData
