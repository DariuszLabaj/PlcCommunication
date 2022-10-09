from datetime import datetime
from enum import IntEnum
from typing import List
from PlcCommunication.NormoSnif._FrameFactory import FrameFactory
from PlcCommunication.NormoSnif import Commands as Cmd
from PlcCommunication.NormoSnif.isDocumentedBy import isDocumentedBy


class NX1P2FrameFactory(FrameFactory):
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

    class RunMode(IntEnum):
        Monitor = 0x02
        Run = 0x04

        def to_bytes(self) -> bytes:
            return self.value.to_bytes(1, "big")

    class ControlerDataType(IntEnum):
        ControllerModel = 0x00
        AreaData = 0x00
        CpuBusUnitConfig = 0x02
        RemoteIO = 0x02
        PcStatus = 0x02

        def to_bytes(self) -> bytes:
            return self.value.to_bytes(1, "big")

    class MemDesignation(FrameFactory._MemAreaDesignation):
        CIO = 0xB0
        WR = 0xB1
        HR = 0xB2
        DM = 0x82

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

    @isDocumentedBy(Cmd.Run)
    def Run(self) -> bytearray:
        return self._generateCommand(Cmd.Run(), 14)

    @isDocumentedBy(Cmd.Stop)
    def Stop(self) -> bytearray:
        return self._generateCommand(Cmd.Stop(), 14)

    @isDocumentedBy(Cmd.Reset)
    def Reset(self) -> bytearray:
        return self._generateCommand(Cmd.Reset(), 14)

    @isDocumentedBy(Cmd.ControllerDataRead)
    def ControllerDataRead(self) -> bytearray:
        return self._generateCommand(
            Cmd.ControllerDataRead(), 10 + 4 + 20 + 20 + 40 + 12 + 64 + 2
        )

    @isDocumentedBy(Cmd.ConnectionDataRead)
    def ConnectionDataRead(self, unitAddress: int, noOfUnits: int) -> bytearray:
        return self._generateCommand(
            Cmd.ConnectionDataRead(unitAddress, noOfUnits), 4096
        )

    @isDocumentedBy(Cmd.ControllerStatusRead)
    def ControllerStatusRead(self) -> bytearray:
        return self._generateCommand(Cmd.ControllerStatusRead(), 4096)

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

    @isDocumentedBy(Cmd.BroadcastTestDataSend)
    def BroadcastTestDataSend(self, testData: bytes) -> bytearray:
        return self._generateCommand(
            Cmd.BroadcastTestDataSend(testData), 14 + len(testData)
        )

    @isDocumentedBy(Cmd.ForcedSetReset)
    def ForcedSetReset(
        self, types: List[int], mem_area_codes: List[int], bits_flags: List[int]
    ) -> bytearray:
        return self._generateCommand(
            Cmd.ForcedSetReset(types, mem_area_codes, bits_flags), 14
        )
