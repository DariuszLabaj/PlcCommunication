from typing import List
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def MessageClear(messagesToClear: List[int]) -> bytes:
    """
    Clears messages generated with MSG(195).
    Message no. parameter (command and response): In the command block, turn ON (1) the bits of the messages to be
    read. In the response block, the bits of the messages being returned will be ON (1). If no bits are turned ON
    in the command block, all bits will be OFF (0) in the response block and no further data will be returned.\n
    messages number 0-7 dec
    """
    messages = 0x40_00
    for message in messagesToClear:
        if message not in range(8):
            raise ValueError("message number incorrect")
        else:
            messages += 2**message

    commandData = CmdBytes.MessageRead.to_bytes()
    commandData += messages.to_bytes(2, "big")
    return commandData
