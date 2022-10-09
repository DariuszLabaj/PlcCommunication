from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def InternodeEchoTest(testData: bytes) -> bytes:
    """
    Performs a internode echo test with the indicated node.\n
    Test data (command and response): Up to 512 bytes of test data can be included in the command. This data is
    transmitted to the indicated node and returned unchanged if communications are normal. If the data returned
    in the response differs from that transmitted in the command, an error occurred in the test\n
    """
    if len(testData) > 512:
        raise ValueError("testData can have maximum size of 512 bytes")
    commandData = CmdBytes.BcasTestDataSend.to_bytes()
    commandData += testData
    return commandData
