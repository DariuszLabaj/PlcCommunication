from typing import Protocol
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


class RunMode(Protocol):
    value: int

    def to_bytes(self) -> bytes:
        return self.value.to_bytes(1, "big")


def Run(mode: RunMode = None, programNo: int = None) -> bytes:
    """
    Changes the PC to MONITOR or RUN mode, enabling the PC to execute its program.
    """
    commandData = CmdBytes.Run.to_bytes()
    commandData += programNo.to_bytes(2, "big")
    if mode:
        commandData += mode.to_bytes()
    return commandData
