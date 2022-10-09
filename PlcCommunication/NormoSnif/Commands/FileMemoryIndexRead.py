from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def FileMemoryIndexRead(beginingBlockNo: int, noOfBlocks: int) -> bytes:
    """
    Reads the File Memory index for the specified number of blocks from the specified beginning block number.\n
    Beginning block number and Number of blocks (command): Set the number of the first block and the total number of
    blocks whose index is to be read. The first block can be 0000 to 07CF (0 to 1999 decimal); the number of blocks
    can be 01 to 80 (1 to 128 decimal).\n
    Number of blocks remaining and Total number of blocks (response): The number of blocks not to be read (0000 to
    07D0 (0 to 2,000 in decimal)) and the total number of blocks in File Memory (0000, 03E8, or 07D0 (0, 1,000, or
    2,000 in decimal, respectively)).\n
    Type (response): The type of File Memory being used.\n
        00: RAM\n
        01: First half RAM; second half ROM\n
    Data type and Control data (response): One byte for each parameter is returned with each block read.\n
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
    Control data: The numbet of comments. Used for comments data only
    """
    if beginingBlockNo > 0xFFFF:
        raise ValueError("beginingBlockNo - must be less then 0x10000")
    if noOfBlocks > 0xFF:
        raise ValueError("noOfBlocks - must ve less then 0x100")
    return (
        CmdBytes.FileMemIndexRead.to_bytes()
        + beginingBlockNo.to_bytes(2, "big")
        + noOfBlocks.to_bytes(1, "big")
    )
