from enum import Enum
from PlcCommunication.NormoSnif.Commands.AccessRightAquire import AccessRightAquire
from PlcCommunication.NormoSnif.Commands.AccessRightForcedAquire import (
    AccessRightForcedAquire,
)
from PlcCommunication.NormoSnif.Commands.AccessRightRelease import AccessRightRelease
from PlcCommunication.NormoSnif.Commands.BroadcastTestDataSend import (
    BroadcastTestDataSend,
)
from PlcCommunication.NormoSnif.Commands.BroadcastTestResultsRead import (
    BroadcastTestResultsRead,
)
from PlcCommunication.NormoSnif.Commands.ClockRead import ClockRead
from PlcCommunication.NormoSnif.Commands.ClockWrite import ClockWrite
from PlcCommunication.NormoSnif.Commands.ConnectionDataRead import ConnectionDataRead
from PlcCommunication.NormoSnif.Commands.ControllerDataRead import (
    ControllerDataRead,
    ControlerDataType,
)
from PlcCommunication.NormoSnif.Commands.ControllerStatusRead import (
    ControllerStatusRead,
)
from PlcCommunication.NormoSnif.Commands.CycleTimeRead import CycleTimeRead
from PlcCommunication.NormoSnif.Commands.DataLinkStatusRead import DataLinkStatusRead
from PlcCommunication.NormoSnif.Commands.DataLinkTableRead import DataLinkTableRead
from PlcCommunication.NormoSnif.Commands.DataLinkTableWrite import DataLinkTableWrite
from PlcCommunication.NormoSnif.Commands.ErrorClear import ErrorClear
from PlcCommunication.NormoSnif.Commands.ErrorLogClear import ErrorLogClear
from PlcCommunication.NormoSnif.Commands.ErrorLogRead import ErrorLogRead
from PlcCommunication.NormoSnif.Commands.FalFalsRead import FalFalsRead
from PlcCommunication.NormoSnif.Commands.FileMemoryIndexRead import FileMemoryIndexRead
from PlcCommunication.NormoSnif.Commands.FileMemoryRead import FileMemoryRead
from PlcCommunication.NormoSnif.Commands.FileMemoryWrite import FileMemoryWrite
from PlcCommunication.NormoSnif.Commands.ForcedSetReset import ForcedSetReset
from PlcCommunication.NormoSnif.Commands.ForcedSetResetCancel import (
    ForcedSetResetCancel,
)
from PlcCommunication.NormoSnif.Commands.InternodeEchoTest import InternodeEchoTest
from PlcCommunication.NormoSnif.Commands.LoopBackTest import LoopBackTest
from PlcCommunication.NormoSnif.Commands.MemoryAreaFill import MemoryAreaFill
from PlcCommunication.NormoSnif.Commands.MemoryAreaRead import MemoryAreaRead
from PlcCommunication.NormoSnif.Commands.MemoryAreaTransfer import MemoryAreaTransfer
from PlcCommunication.NormoSnif.Commands.MemoryAreaWrite import MemoryAreaWrite
from PlcCommunication.NormoSnif.Commands.MessageClear import MessageClear
from PlcCommunication.NormoSnif.Commands.MessageRead import MessageRead
from PlcCommunication.NormoSnif.Commands.MultipleMemoryAreaRead import (
    MultipleMemoryAreaRead,
)
from PlcCommunication.NormoSnif.Commands.MultipointForcedStatusRead import (
    MultipointForcedStatusRead,
)
from PlcCommunication.NormoSnif.Commands.NameDelete import NameDelete
from PlcCommunication.NormoSnif.Commands.NameRead import NameRead
from PlcCommunication.NormoSnif.Commands.NameSet import NameSet
from PlcCommunication.NormoSnif.Commands.NetworkStatusRead import NetworkStatusRead
from PlcCommunication.NormoSnif.Commands.ParameterAreaClear import ParameterAreaClear
from PlcCommunication.NormoSnif.Commands.ParameterAreaRead import ParameterAreaRead
from PlcCommunication.NormoSnif.Commands.ParameterAreaWrite import ParameterAreaWrite
from PlcCommunication.NormoSnif.Commands.ProgramAreaClear import ProgramAreaClear
from PlcCommunication.NormoSnif.Commands.ProgramAreaProtect import ProgramAreaProtect
from PlcCommunication.NormoSnif.Commands.ProgramAreaProtectClear import (
    ProgramAreaProtectClear,
)
from PlcCommunication.NormoSnif.Commands.ProgramAreaRead import ProgramAreaRead
from PlcCommunication.NormoSnif.Commands.ProgramAreaWrite import ProgramAreaWrite
from PlcCommunication.NormoSnif.Commands.Reset import Reset
from PlcCommunication.NormoSnif.Commands.Run import Run, RunMode
from PlcCommunication.NormoSnif.Commands.Stop import Stop


class CommandList(Enum):
    MemAreaRead = b"\x01\x01"
    MemAreaWrite = b"\x01\x02"
    MemAreaFill = b"\x01\x03"
    MulMemAreaRead = b"\x01\x04"
    MemAreaTran = b"\x01\x05"
    ParmAreaRead = b"\x02\x01"
    ParmAreaWrite = b"\x02\x02"
    ParamAreaClear = b"\x02\x03"
    DataLinkTableRead = b"\x02\x20"
    DataLinkTableWrite = b"\x02\x21"
    ProgAreaProtect = b"\x03\x04"
    ProgAreaProcClear = b"\x03\x05"
    ProgAreaRead = b"\x03\x06"
    ProgAreaWrite = b"\x03\x07"
    ProgAreaClear = b"\x03\x08"
    Run = b"\x04\x01"
    Stop = b"\x04\x02"
    Reset = b"\x04\x03"
    CtrDataRead = b"\x05\x01"
    ConnDataRead = b"\x05\x02"
    CtrStatRead = b"\x06\x01"
    NetStatRead = b"\x06\x02"
    DLinkStatRead = b"\x06\x03"
    CTimeRead = b"\x06\x20"
    ClockRead = b"\x07\x01"
    ClockWrite = b"\x07\x02"
    BcasTestDataSend = b"\x08\x01"
    BcastTestResultsRead = b"\x08\x02"
    MessageRead = b"\x09\x20"
    AccessRightAq = b"\x0C\x01"
    AccessRightFAq = b"\x0C\x02"
    AccessRightRel = b"\x0C\x03"
    ErrorClear = b"\x21\x01"
    ErrorLogRead = b"\x21\x02"
    ErrorLogClear = b"\x21\x03"
    FileMemIndexRead = b"\x22\x0F"
    FileMemRead = b"\x22\x10"
    FileMemWrite = b"\x22\x11"
    ForceSetReset = b"\x23\x01"
    ForceSetResetCancel = b"\x23\x02"
    MulPointForceStatusRead = b"\x23\x0A"
    NameSet = b"\x26\x01"
    NameDel = b"\x26\x02"
    NameRead = b"\x26\x03"
    Unknown = None

    @staticmethod
    def from_bytes(data: bytes):
        try:
            return CommandList(data)
        except ValueError:
            return CommandList.Unknown


if __name__ == "__main__":
    help(AccessRightAquire)
    help(AccessRightForcedAquire)
    help(AccessRightRelease)
    help(BroadcastTestDataSend)
    help(BroadcastTestResultsRead)
    help(ClockRead)
    help(ClockWrite)
    help(ConnectionDataRead)
    help(ControllerDataRead)
    help(ControlerDataType)
    help(ControllerStatusRead)
    help(CycleTimeRead)
    help(DataLinkStatusRead)
    help(DataLinkTableRead)
    help(DataLinkTableWrite)
    help(ErrorClear)
    help(ErrorLogClear)
    help(ErrorLogRead)
    help(FalFalsRead)
    help(FileMemoryIndexRead)
    help(FileMemoryRead)
    help(FileMemoryWrite)
    help(ForcedSetReset)
    help(ForcedSetResetCancel)
    help(InternodeEchoTest)
    help(LoopBackTest)
    help(MemoryAreaFill)
    help(MemoryAreaRead)
    help(MemoryAreaTransfer)
    help(MemoryAreaWrite)
    help(MessageClear)
    help(MessageRead)
    help(MultipleMemoryAreaRead)
    help(MultipointForcedStatusRead)
    help(NameDelete)
    help(NameRead)
    help(NameSet)
    help(NetworkStatusRead)
    help(ParameterAreaClear)
    help(ParameterAreaRead)
    help(ParameterAreaWrite)
    help(ProgramAreaClear)
    help(ProgramAreaProtect)
    help(ProgramAreaProtectClear)
    help(ProgramAreaRead)
    help(ProgramAreaWrite)
    help(Reset)
    help(Run)
    help(RunMode)
    help(Stop)
