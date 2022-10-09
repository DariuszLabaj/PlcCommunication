from datetime import datetime
from typing import List
from PlcCommunication.NormoSnif._FrameFactory import FrameFactory
from PlcCommunication.NormoSnif import Commands as Cmd
from PlcCommunication.NormoSnif.isDocumentedBy import isDocumentedBy


class GeneralFrameFactory(FrameFactory):
    def __init__(
        self,
        responseFrame: bool = False,
        responseNotRequired: bool = False,
        destinationNetworkAddress: int = 0,
        destinationNodeNumber: int = 0xFF,
        destinationUnitAddress: int = 0,
        sourceNetworkAddress: int = 0,
        sourceNodeNumber: int = 0x7E,
        sourceUnitAddress: int = 0,
    ):
        super().__init__(
            responseFrame,
            responseNotRequired,
            destinationNetworkAddress,
            destinationNodeNumber,
            destinationUnitAddress,
            sourceNetworkAddress,
            sourceNodeNumber,
            sourceUnitAddress,
        )

    class RunMode(Cmd.RunMode):
        pass

    class ControlerDataType(Cmd.ControlerDataType):
        pass

    class MemDesignation(FrameFactory._MemAreaDesignation):
        CIO = 0xB0
        WR = 0xB1
        HR = 0xB2
        DM = 0x82
        EM0 = 0x50
        EM1 = 0x51
        EM2 = 0x52
        EM3 = 0x53
        EM4 = 0x54
        EM5 = 0x55
        EM6 = 0x56
        EM7 = 0x57
        EM8 = 0x58
        EM9 = 0x59
        EMA = 0x5A
        EMB = 0x5B
        EMC = 0x5C
        EMD = 0x5D
        EME = 0x5E
        EMF = 0x5F
        EM10 = 0x60
        EM11 = 0x61
        EM12 = 0x62
        EM13 = 0x63
        EM14 = 0x64
        EM15 = 0x65
        EM16 = 0x66
        EM17 = 0x67
        EM18 = 0x68

    class ParamDesignation(FrameFactory._ParamAreaDesignation):
        PC_Setup = 0x8010
        PeripheralDeviceSettings = 0x8011
        IO_Table = 0x8012
        Routing_Table_Area = 0x8013
        CPU_BusUnit_Settings = 0x8002

    @isDocumentedBy(Cmd.MemoryAreaRead)
    def MemoryAreaRead(
        self, areaCode: MemDesignation, beginningAddress: int, noOfITems: int
    ) -> bytearray:
        return self._generateCommand(
            Cmd.MemoryAreaRead(areaCode, beginningAddress, noOfITems),
            noOfITems * 2 + 14,
        )

    @isDocumentedBy(Cmd.MemoryAreaWrite)
    def MemoryAreaWrite(
        self,
        areaCode: MemDesignation,
        beginAddress: int,
        dataAray: bytearray,
    ) -> bytearray:
        return self._generateCommand(
            Cmd.MemoryAreaWrite(areaCode, beginAddress, dataAray), 14
        )

    @isDocumentedBy(Cmd.MemoryAreaFill)
    def MemoryAreaFill(
        self,
        areaCode: MemDesignation,
        beginningAddress: int,
        noOfItems: int,
        data: int,
    ) -> bytearray:
        return self._generateCommand(
            Cmd.MemoryAreaFill(areaCode, beginningAddress, noOfItems, data), 14
        )

    @isDocumentedBy(Cmd.MultipleMemoryAreaRead)
    def MultipleMemoryAreaRead(
        self, areaCodes: List[MemDesignation], beginningAddress: List[int]
    ) -> bytearray:
        return self._generateCommand(
            Cmd.MultipleMemoryAreaRead(areaCodes, beginningAddress),
            len(areaCodes) * 3 + 14,
        )

    @isDocumentedBy(Cmd.MemoryAreaTransfer)
    def MemoryAreaTransfer(
        self,
        areaCodes: List[MemDesignation],
        beginningAddress: List[int],
        noOfItems: int,
    ) -> bytearray:
        return self._generateCommand(
            Cmd.MemoryAreaTransfer(areaCodes, beginningAddress, noOfItems), 14
        )

    @isDocumentedBy(Cmd.ParameterAreaRead)
    def ParameterAreaRead(
        self, areaCodes: ParamDesignation, beginningWord: int, noOfWords: int
    ) -> bytearray:
        return self._generateCommand(
            Cmd.ParameterAreaRead(areaCodes, beginningWord, noOfWords),
            noOfWords * 2 + 20,
        )

    @isDocumentedBy(Cmd.ParameterAreaWrite)
    def ParameterAreaWrite(
        self,
        areaCodes: ParamDesignation,
        beginningWord: int,
        noOfWords: int,
        data: List[int],
    ) -> bytearray:
        return self._generateCommand(
            Cmd.ParameterAreaWrite(areaCodes, beginningWord, noOfWords, data), 14
        )

    @isDocumentedBy(Cmd.ParameterAreaClear)
    def ParameterAreaClear(
        self, areaCodes: ParamDesignation, noOfWords: int
    ) -> bytearray:
        return self._generateCommand(Cmd.ParameterAreaClear(areaCodes, noOfWords), 14)

    @isDocumentedBy(Cmd.DataLinkTableRead)
    def DataLinkTableRead(self, readLength: int) -> bytearray:
        return self._generateCommand(Cmd.DataLinkTableRead(readLength), 4096)

    @isDocumentedBy(Cmd.DataLinkTableWrite)
    def DataLinkTableWrite(
        self,
        writeLength: int,
        noOfLinkNodes,
        nodeNo: List[int],
        cioFirstWord: List[int],
        dmFirstWord: List[int],
        noOfTotalWords: List[int],
    ) -> bytearray:
        return self._generateCommand(
            Cmd.DataLinkTableWrite(
                writeLength,
                noOfLinkNodes,
                nodeNo,
                cioFirstWord,
                dmFirstWord,
                noOfTotalWords,
            ),
            4096,
        )

    @isDocumentedBy(Cmd.ProgramAreaProtect)
    def ProgramAreaProtect(self, password: bytearray) -> bytearray:
        return self._generateCommand(Cmd.ProgramAreaProtect(password), 14)

    @isDocumentedBy(Cmd.ProgramAreaProtectClear)
    def ProgramAreaProtectClear(self, password: bytearray) -> bytearray:
        return self._generateCommand(Cmd.ProgramAreaProtectClear(password), 14)

    @isDocumentedBy(Cmd.ProgramAreaRead)
    def ProgramAreaRead(
        self, beginningAddress: int, noOfBytes: int, programNo: int = 0
    ) -> bytearray:
        return self._generateCommand(
            Cmd.ProgramAreaRead(
                beginningAddress, noOfBytes, programNo, noOfBytes * 2 + 10 + 12
            )
        )

    @isDocumentedBy(Cmd.ProgramAreaWrite)
    def ProgramAreaWrite(
        self,
        beginningAddress: int,
        noOfBytes: int,
        data: List[bytes],
        programNo: int = 0,
    ) -> bytearray:
        return self._generateCommand(
            Cmd.ProgramAreaWrite(beginningAddress, noOfBytes, data, programNo), 22
        )

    @isDocumentedBy(Cmd.ProgramAreaClear)
    def ProgramAreaClear(self) -> bytearray:
        return self._generateCommand(Cmd.ProgramAreaClear(), 14)

    @isDocumentedBy(Cmd.Run)
    def Run(self, mode: RunMode = None, programNo: int = None) -> bytearray:
        return self._generateCommand(Cmd.Run(mode, programNo), 14)

    @isDocumentedBy(Cmd.Stop)
    def Stop(self) -> bytearray:
        return self._generateCommand(Cmd.Stop(), 14)

    @isDocumentedBy(Cmd.Reset)
    def Reset(self) -> bytearray:
        return self._generateCommand(Cmd.Reset(), 14)

    @isDocumentedBy(Cmd.ControllerDataRead)
    def ControllerDataRead(self, data: ControlerDataType = None) -> bytearray:
        if data:
            if (
                data
                == Cmd.ControlerDataType.ControllerModel | data
                == Cmd.ControlerDataType.AreaData
            ):
                retbytesNo = 10 + 4 + 20 + 20 + 40 + 12
            else:
                retbytesNo = 10 + 4 + 64 + 2
        else:
            retbytesNo = 10 + 4 + 20 + 20 + 40 + 12 + 64 + 2
        return self._generateCommand(Cmd.ControllerDataRead(data), retbytesNo)

    @isDocumentedBy(Cmd.ConnectionDataRead)
    def ConnectionDataRead(self, unitAddress: int, noOfUnits: int) -> bytearray:
        return self._generateCommand(
            Cmd.ConnectionDataRead(unitAddress, noOfUnits), 4096
        )

    @isDocumentedBy(Cmd.ControllerStatusRead)
    def ControllerStatusRead(self) -> bytearray:
        return self._generateCommand(Cmd.ControllerStatusRead(), 4096)

    @isDocumentedBy(Cmd.NetworkStatusRead)
    def NetworkStatusRead(self) -> bytearray:
        return self._generateCommand(Cmd.NetworkStatusRead(), 4096)

    @isDocumentedBy(Cmd.DataLinkStatusRead)
    def DataLinkStatusRead(self) -> bytearray:
        return self._generateCommand(Cmd.DataLinkStatusRead(), 4096)

    @isDocumentedBy(Cmd.CycleTimeRead)
    def CycleTimeRead(self) -> bytearray:
        return self._generateCommand(Cmd.CycleTimeRead(), 14 + 4 + 4 + 4)

    @isDocumentedBy(Cmd.ClockRead)
    def ClockRead(self) -> bytearray:
        return self._generateCommand(Cmd.ClockRead(), 10 + 11)

    @isDocumentedBy(Cmd.ClockWrite)
    def ClockWrite(self, sourceDate: datetime) -> bytearray:
        return self._generateCommand(Cmd.ClockWrite(sourceDate), 14)

    @isDocumentedBy(Cmd.LoopBackTest)
    def LoopBackTest(self, testData: bytes) -> bytearray:
        return self._generateCommand(Cmd.LoopBackTest(testData), 14 + len(testData))

    @isDocumentedBy(Cmd.InternodeEchoTest)
    def InternodeEchoTest(self, testData: bytes) -> bytearray:
        return self._generateCommand(
            Cmd.InternodeEchoTest(testData), 14 + len(testData)
        )

    @isDocumentedBy(Cmd.BroadcastTestResultsRead)
    def BroadcastTestResultsRead(self) -> bytearray:
        return self._generateCommand(Cmd.BroadcastTestResultsRead(), 16)

    @isDocumentedBy(Cmd.BroadcastTestDataSend)
    def BroadcastTestDataSend(self, testData: bytes) -> bytearray:
        return self._generateCommand(
            Cmd.BroadcastTestDataSend(testData), 14 + len(testData)
        )

    @isDocumentedBy(Cmd.MessageRead)
    def MessageRead(self, messagesToRead: List[int]) -> bytearray:
        return self._generateCommand(
            Cmd.MessageRead(messagesToRead), 14 + len(messagesToRead) * 34
        )

    @isDocumentedBy(Cmd.MessageClear)
    def MessageClear(self, messagesToClear: List[int]) -> bytearray:
        return self._generateCommand(Cmd.MessageClear(messagesToClear), 18)

    @isDocumentedBy(Cmd.FalFalsRead)
    def FalFalsRead(self, failNo: int) -> bytearray:
        return self._generateCommand(Cmd.FalFalsRead(failNo), 14 + 2 + 16)

    @isDocumentedBy(Cmd.AccessRightAquire)
    def AccessRightAquire(self) -> bytearray:
        return self._generateCommand(Cmd.AccessRightAquire(), 14 + 3)

    @isDocumentedBy(Cmd.AccessRightForcedAquire)
    def AccessRightForcedAquire(self) -> bytearray:
        return self._generateCommand(Cmd.AccessRightForcedAquire(), 14 + 3)

    @isDocumentedBy(Cmd.AccessRightRelease)
    def AccessRightRelease(self) -> bytearray:
        return self._generateCommand(Cmd.AccessRightRelease(), 14 + 3)

    @isDocumentedBy(Cmd.ErrorClear)
    def ErrorClear(self, failNo: int) -> bytearray:
        return self._generateCommand(Cmd.ErrorClear(failNo), 14)

    @isDocumentedBy(Cmd.ErrorLogRead)
    def ErrorLogRead(self, beginningRecordNo: int, noOfRecords: int) -> bytearray:
        return self._generateCommand(
            Cmd.ErrorLogRead(beginningRecordNo, noOfRecords), 14 + 6 + noOfRecords * 10
        )

    @isDocumentedBy(Cmd.ErrorLogClear)
    def ErrorLogClear(self) -> bytearray:
        return self._generateCommand(Cmd.ErrorLogClear(), 14)

    @isDocumentedBy(Cmd.FileMemoryIndexRead)
    def FileMemoryIndexRead(self, beginingBlockNo: int, noOfBlocks: int) -> bytearray:
        return self._generateCommand(
            Cmd.FileMemoryIndexRead(beginingBlockNo, noOfBlocks),
            14 + 5 + noOfBlocks * 2,
        )

    @isDocumentedBy(Cmd.FileMemoryRead)
    def FileMemoryRead(self, blockNo: int) -> bytearray:
        return self._generateCommand(Cmd.FileMemoryRead(blockNo), 14 + 2 + 256)

    @isDocumentedBy(Cmd.FileMemoryWrite)
    def FileMemoryWrite(
        self,
        data_type: int,
        blockNo: int,
        data: bytes,
        protected: bool = False,
        contain_end: bool = False,
    ) -> bytearray:
        return self._generateCommand(
            Cmd.FileMemoryWrite(data_type, blockNo, data, protected, contain_end), 14
        )

    @isDocumentedBy(Cmd.ForcedSetReset)
    def ForcedSetReset(
        self, types: List[int], mem_area_codes: List[int], bits_flags: List[int]
    ) -> bytearray:
        return self._generateCommand(
            Cmd.ForcedSetReset(types, mem_area_codes, bits_flags), 14
        )

    @isDocumentedBy(Cmd.ForcedSetResetCancel)
    def ForcedSetResetCancel(self) -> bytearray:
        return self._generateCommand(Cmd.ForcedSetResetCancel(), 14)

    @isDocumentedBy(Cmd.MultipointForcedStatusRead)
    def MultipointForcedStatusRead(
        self, areaCode: MemDesignation, beginningAddress: int, noOfUnits: int
    ) -> bytearray:
        return self._generateCommand(
            Cmd.MultipointForcedStatusRead(areaCode, beginningAddress, noOfUnits),
            14 + 1 + 3 + 2 + noOfUnits * 2,
        )

    @isDocumentedBy(Cmd.NameSet)
    def NameSet(self, nameData: str) -> bytearray:
        return self._generateCommand(Cmd.NameSet(nameData), 14)

    @isDocumentedBy(Cmd.NameDelete)
    def NameDelete(self) -> bytearray:
        return self._generateCommand(Cmd.NameDelete(), 14)

    @isDocumentedBy(Cmd.NameRead)
    def NameRead(self) -> bytearray:
        return self._generateCommand(Cmd.NameRead(), 14)
