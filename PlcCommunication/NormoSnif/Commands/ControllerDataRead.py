from typing import Protocol
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


class ControlerDataType(Protocol):
    value: int

    def to_bytes(self) -> bytes:
        return self.value.to_bytes(1, "big")


def ControllerDataRead(data: ControlerDataType = None) -> bytes:
    """
    Reads the following data:\n
    • Controller model and version\n
    • Area data\n
    • CPU Bus Unit configuration\n
    • Remote I/O data\n
    • PC status\n
    Data (command): Specify as follows to read the desired data:\n
    00 - Controller model, Controller version, Area data\n
    02 - CPU Bus Unit configuration, Remote I/O data,PC status
    """
    commandData = CmdBytes.CtrDataRead.to_bytes()
    if data:
        commandData += data.to_bytes()
    return commandData
