from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def DataLinkTableRead(readLength: int) -> bytes:
    """
    Reads the contents of the data link table.\n
    Intelligent ID no. (command): Designate S (53) and N (4E) in ASCII.\n
    Beginning word (command): Set to 0000.\n
    Read length (command): Regardless of the value that you designate, the data link tables for the number of link
    nodes that has been set will be read.\n
    No. of link nodes (response): The number of link nodes set in the data link table will be returned; the
    configuration is as follows (bit 7 is always set to 1)\n
    One-block record (response): One-block records will be returned in sequence according to the setting order in
    the data link table (in the case of automatic setting, they will be returned in node number order). The total
    number of bytes required is as follows:\n
    • Node Number The configuration of a node number is shown below. It expresses the status of the data link node
    number of the one-block record and the data link on the node.\n
    • CIO Area First Word The first word in a data link in the CIO Area\n
    • Kind of DM Set to 00\n
    • DM Area First Word The first word of a data link in the DM Area.\n
    • No. of Total Words The total number of words of the CIO and DM Area varies with the block as follows:\n
    1st block: The total number of data link words in the CIO Area.\n
    2nd block: The total number of data link words in the DM Area.\n
    Other blocks: Set to 0000.
    """
    if readLength < 1:
        raise ValueError("readLength - must be grather then 0")
    commandData = CmdBytes.DataLinkTableRead.to_bytes()  # Set command bytes
    commandData += b"\x00\x00\x53\x4E\x00\x00"
    commandData += readLength.to_bytes(2, "big")  # Set Number of items to write
    return commandData
