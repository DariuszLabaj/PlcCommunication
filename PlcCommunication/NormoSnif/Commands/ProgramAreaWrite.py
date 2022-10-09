from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ProgramAreaWrite(
    beginningAddress: int,
    noOfBytes: int,
    data: bytearray,
    programNo: int = 0,
) -> bytes:
    """
    Writes data to the specified number of consecutive program area words
    starting from the specified word. A maximum of 512 bytes can be written
    with each command. To write larger amounts of data, use multiple commands
    and specify the beginning word and number of words for each.\n
    -- Program no. -- (command and response): Set to 0000.\n
    -- Beginning word -- (command and response): Set a relative byte address with
    00000000 as the starting address. The beginning word must be an even number.
    The address set in the command will be returned in the response.\n
    -- No. of bytes -- (command and response): The number of bytes in an even number
    (512 or smaller). The number of bytes actually written will be returned in the
    response. Bit 15 must be turned ON (1) when data for the last write to the
    program area so that the PC can generate an index. To write only an index marker,
    specify 8000 for the number of bytes.
    """
    if noOfBytes < 1:
        raise ValueError("noOfBytes - must be grather then 0")
    commandData = CmdBytes.ProgAreaWrite.to_bytes()
    commandData += programNo.to_bytes(2, "big")
    commandData += beginningAddress.to_bytes(4, "big")
    commandData += noOfBytes.to_bytes(2, "big")
    commandData += bytes(data)
    return commandData
