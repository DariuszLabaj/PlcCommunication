from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def BroadcastTestResultsRead() -> bytes:
    """
    Reads the results (number of receptions for each node) of the broadcast tests carried out using the BROADCAST
    TEST DATA SEND command. Refer to BROADCAST TEST DATA SEND for details on that command\n
    Number of receptions (response): The number of times that the BROADCAST TEST DATA SEND command has been executed
    since the last BROADCAST TEST RESULTS READ command was executed.\n
    When this command is executed, the number of receptions data stored in the destination nodes is cleared. If the
    number of receptions does not equal the number of times that the BROADCAST TEST DATA SEND command has been
    executed since the last BROADCAST TEST RESULTS READ command was executed, an error has occurred.
    """
    return CmdBytes.BcastTestResultsRead.to_bytes()
