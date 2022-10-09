from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def FileMemoryRead(blockNo: int) -> bytes:
    """
    Reads the contents of the specified File Memory block\n
    Block number (command): Specify the number of the File Memory block to read between 0000 and 07CF (0 and 1,999
    in decimal).\n
    Data type and Control data (response): One byte for each index parameter is returned with each block read.\n
    Data type: As follows:
    Data type: As follows:\n
        Bit 7 : 1: Block containg END(01)(for user programs only)
        Bit 6 : 1: Protected
        bit 5..3 : 0
        Bit 2..0 : ...\n
            2   1   0   Data type\n
            0   0   0   Empty\n
            0   0   1   I/O data\n
            0   1   0   User Program\n
            0   1   1   Comments\n
    Control data: The numbet of comments. Used for comments data only\n
    Data (response): The contents of the specified File Memory block (256 bytes (128 words).
    """
    if blockNo > 1999:
        raise ValueError(
            "Specify the number of the File Memory block to read between 0000 and 07CF (0 and 1,999 in decimal)"
        )
    return CmdBytes.FileMemRead.to_bytes() + blockNo.to_bytes(2, "big")
