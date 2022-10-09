from abc import ABC
from enum import IntEnum
from functools import cached_property
from typing import List, Tuple
from PlcCommunication.NormoSnif.Commands import CommandList
from PlcCommunication.NormoSnif.ErrorCode import ErrorCode

from PlcCommunication.NormoSnif.Frame import CommandFrame


class DestinationNetworkAddresOutOfRangeException(ValueError):
    ...


class DestinationNodeNumberOutOfRangeException(ValueError):
    ...


class DestinationUnitAddressOutOFRangeException(ValueError):
    ...


class SourceNetworkAddresOutOfRangeException(ValueError):
    ...


class SourceNodeNumberOutOfRangeException(ValueError):
    ...


class SourceUnitAddressOutOfRangeException(ValueError):
    ...


class FrameFactory(ABC):
    @cached_property
    def IdTag(self) -> bytes:
        return bytes(bytearray([self.SNA, self.SA1, self.SA2]))

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
        """
        Command Data Structure\n
        | ICF | RSV | GCT | DNA | DA1 | DA2 | SNA | SA1 | SA2 | SID | CMD | CMD | ... |\n
        Response Data Structure\n
        | ICF | RSV | GCT | DNA | DA1 | DA2 | SNA | SA1 | SA2 | SID | CMD | CMD | RSP | RSP | ... |
        """
        """
        ICF     -- Information control field
        bit     7   6   5   4   3   2   1   0
                1   n   0   0   0   0   0   n

                bit7 - Gateway use(0: don't use; 1:use) set to 1
                bit6 - Data type (0:command; 1:response)
                bit5-1 - Set to 0
                bit0 - Response setting(0: response required; 1:response not required)
        """
        self.ICF = (
            0b11000001
            & (int(responseFrame) << 6 | 0b10000001)
            & (int(responseNotRequired) | 0b11000000)
        )
        """
        RSV     -- Reserved. Set to 00
        """
        self.RSV = 0x00
        """
        GCT     -- Gateway count. Set to 02
        """
        self.GCT = 0x02
        """
        DNA     -- Destination network address. Specify within the following ranges
                00:         Local Network
                01 to 7F:   Remote network(1 to 127)
        """
        if 0x7F < destinationNetworkAddress or destinationNetworkAddress < 0:
            raise DestinationNetworkAddresOutOfRangeException(
                """Destination network address. Specify within the
            following ranges\n00:\t\tLocal Network\n01 to 7F:\tRemote network(1 to 127)"""
            )
        self.DNA = destinationNetworkAddress
        """
        DA1     -- Destination node number. Specify within the following ranges.
                01 to 7E:   Node number in SYSMAC NET network(1 to 126 decimal)
                01 to 3E:   Node number in SYSMAC LINK network(1 to 62 decimal)
                FF: Broadcast transmission
        """
        if (
            0x7E < destinationNodeNumber or destinationNodeNumber < 1
        ) and destinationNodeNumber != 0xFF:
            raise DestinationNodeNumberOutOfRangeException(
                """Destination node number. Specify within the following ranges.\n01 to 7E:   Node number in SYSMAC NET
                network(1 to 126 decimal)\n01 to 3E:   Node number in SYSMAC LINK network(1 to 62 decimal)\nFF:
                Broadcast transmission"""
            )
        self.DA1 = destinationNodeNumber
        """
        DA2     -- Destination unit address. Specify within the following ranges.
                00:         PC (CPU)
                FE:         SYSMAC NET Link Unit or SYSMAC LINK Unit connected to network
                10 to 1F:   CPU Bus Unit(10 + unit number in hexadecimal)
        """
        if (
            (0x10 < destinationUnitAddress or destinationUnitAddress > 0x1F)
            and destinationUnitAddress != 0x00
            and destinationUnitAddress != 0xFE
        ):
            raise DestinationUnitAddressOutOFRangeException(
                """Destination unit address. Specify within the following ranges.\n00:         PC (CPU)\n
                FE:         SYSMAC NET Link Unit or SYSMAC LINK Unit connected to network\n10 to 1F:   CPU Bus Unit(10 +
                unit number in hexadecimal)"""
            )
        self.DA2 = destinationUnitAddress
        """
        SNA     -- Source network address. Specify within the following ranges.
                00:         Local network
                01 to 7F:   Remote network(1 to 127 decimal)
        """
        if 0x7F < sourceNetworkAddress or sourceNetworkAddress < 0:
            raise SourceNetworkAddresOutOfRangeException(
                """Source network address. Specify within the following ranges.
            \n00:         Local network\n01 to 7F:   Remote network(1 to 127 decimal)"""
            )
        self.SNA = sourceNetworkAddress
        """
        SA1     -- Source node number. Specify within the following ranges.
                01 to 7E:   Node number in SYSMAC NET network(1 to 126 decimal)
                01 to 3E:   Node number in SYSMAC LINK network(1 to 62 decimal)
                FF:         Broadcast transmission
        """
        if (
            0x7F < sourceNodeNumber or sourceNodeNumber < 0x01
        ) and sourceNodeNumber != 0xFF:
            raise SourceNodeNumberOutOfRangeException(
                """Source node number. Specify within the following ranges.\n01 to
            7E:   Node number in SYSMAC NET network(1 to 126 decimal)\n01 to 3E:   Node number in SYSMAC LINK network(1
            to 62 decimal)\nFF:         Broadcast transmission"""
            )
        self.SA1 = sourceNodeNumber
        """
        SA2     -- Source unit address. Specify within the following ranges.
                00:         PC (CPU)
                FE:         SYSMAC NET Link Unit or SYSMAC LINK Unit connected to network
                10 to 1F:   CPU Bus Unit(10 + unit number in hexadecimal)
        """
        if (
            (0x10 < sourceUnitAddress or sourceUnitAddress > 0x1F)
            and sourceUnitAddress != 0xFE
            and sourceUnitAddress != 0x0
        ):
            raise SourceUnitAddressOutOfRangeException(
                """Source unit address. Specify within the following ranges.\n00:
            PC (CPU)\nFE:         SYSMAC NET Link Unit or SYSMAC LINK Unit connected to network\n10 to 1F:   CPU Bus
            Unit(10 + unit number in hexadecimal)"""
            )
        self.SA2 = sourceUnitAddress
        """
        SID     -- Service ID. Used to identify the processing generating the transmission. Set the
                SID to any number between 00 and FF

                Note The unit address for CPU Bus Unit is 10 (hexadecimal) plus the unit number
                    set on the front panel of the CPU Bus Unit
        """
        self.SID = 0x00

    def _parseFrameBytes(self, data: bytes) -> Tuple[CommandList, bytes]:
        if (
            data is None or len(data) < 12
        ):  # check if there are bytes to parse and length of them is minimum 12
            return CommandList.Unknown, b""
        DataSent = data[6:9] == self.IdTag  # chceck wheater freame was sent
        DataReceived = data[3:6] == self.IdTag  # chceck wheater freame was received
        if not DataSent and not DataReceived:
            return CommandList.Unknown, b""
        command = CommandList.from_bytes(data[10:12])  # get the command used
        if command == CommandList.Unknown:
            return CommandList.Unknown, b""
        parsedData = data[12:]  # get the data
        return command, parsedData

    def validateFrames(
        self, sentFrame: bytes, receivedFrame: bytes
    ) -> Tuple[ErrorCode, bytes]:
        CmdSent, _ = self._parseFrameBytes(sentFrame)
        CmdRcv, RcvData = self._parseFrameBytes(receivedFrame)
        if (
            not RcvData
            or CmdSent != CmdRcv
            or CmdSent == CommandList.Unknown
            or CmdRcv == CommandList.Unknown
        ):
            return ErrorCode.from_bytes(b"\xFF\xFE"), b""
        return ErrorCode.from_bytes(RcvData[:2]), RcvData[2:]

    def _incrementSID(self):
        if self.SID >= 0xFF:
            self.SID = 0x00
        else:
            self.SID += 1

    def _generateCommand(
        self, data: bytes | bytearray | List[int], rcvSize: int
    ) -> CommandFrame:
        self._incrementSID()
        commandData = bytearray(
            [
                self.ICF,
                self.RSV,
                self.GCT,
                self.DNA,
                self.DA1,
                self.DA2,
                self.SNA,
                self.SA1,
                self.SA2,
                self.SID,
            ]
        )
        for byte in data:
            commandData.append(byte)
        return CommandFrame(commandData, rcvSize)

    class _MemAreaDesignation(IntEnum):
        def to_bytes(self) -> bytes:
            return self.value.to_bytes(1, "big")

    class _ParamAreaDesignation(IntEnum):
        def to_bytes(self) -> bytes:
            return self.value.to_bytes(2, "big")
