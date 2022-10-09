from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def FileMemoryWrite(
    data_type: int,
    blockNo: int,
    data: bytes,
    protected: bool = False,
    contain_end: bool = False,
) -> bytes:
    """
    Writes the specified contents to the specified File Memory block\n
    Data type and Control data (command): Specify one byte for each index parameter.\n
    Data type: Specify as follows:\n
        Bit 7 : 1: Block containg END(01)(for user programs only)*Turn ON (1) this bit only for a block containing
        END(01) or a final block\n
        Bit 6 : 1: Protected\n
        bit 5..3 : 0\n
        Bit 2..0 : ...\n
            2   1   0   Data type\n
            0   0   0   Empty\n
            0   0   1   I/O data\n
            0   1   0   User Program\n
            0   1   1   Comments\n
    Control data: Specify the number of comments. Used for comment data only. Control data specified for other data
    types will be ignored.\n
    Block number (command): Specify the number of the File Memory block to write between 0000 and 07CF (0 and 1,999
    blocks).\n
    Data (command): Specify the contents for the specified File Memory block (256 bytes (128 words).
    """
    if blockNo > 1999:
        raise ValueError(
            "Specify the number of the File Memory block to write between 0000 and 07CF (0 and 1,999 blocks)"
        )
    if len(data) > 256 or len(data) < 1:
        raise ValueError(
            "Specify the contents for the specified File Memory block (256 bytes (128 words)"
        )
    control_data = 0
    if data_type & 3 == 3:
        control_data = len(data)
    if contain_end:
        data_type = data_type | 128
    if protected:
        data_type = data_type | 64
    commandData = CmdBytes.FileMemWrite.to_bytes()
    commandData += data_type.to_bytes(1, "big")
    commandData += control_data.to_bytes(1, "big")
    commandData += data
    return commandData
