from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def LoopBackTest(testData: bytes) -> bytes:
    """
    Executes a loop-back test between the local node and a destination node.
    Test data (command and response): In the command block, designate the data to be transmitted to the destination
    node. The designated data consists of 1,986 bytes maximum (binary data). In the response block, the test data
    from the command block will be returned as it is. If the test data in the response block is different from that
    in the command block, an error has occurred. Reads the error log file.
    """
    if len(testData) > 1986:
        raise ValueError("testData can have maximum size of 1986 bytes")
    commandData = CmdBytes.BcasTestDataSend.to_bytes()
    commandData += testData
    return commandData
