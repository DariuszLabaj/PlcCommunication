from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def BroadcastTestDataSend(testData: bytes) -> bytes:
    """
    Sends the test data in the command to all nodes in the specified network. No response will be returned when this
    command is executed, but reception of the test data can be verified by executing the BROADCAST TEST RESULTS READ
    command. Refer to BROADCAST TEST RESULTS READ for details.
    """
    if len(testData) > 1986:
        raise ValueError("testData can have maximum size of 1986 bytes")
    commandData = CmdBytes.BcasTestDataSend.to_bytes()
    commandData += testData
    return commandData
