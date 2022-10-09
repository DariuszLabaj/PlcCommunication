from enum import IntEnum


class CmdBytes(IntEnum):
    MemAreaRead = 0x0101
    MemAreaWrite = 0x0102
    MemAreaFill = 0x0103
    MulMemAreaRead = 0x0104
    MemAreaTran = 0x0105
    ParmAreaRead = 0x0201
    ParmAreaWrite = 0x0202
    ParamAreaClear = 0x0203
    DataLinkTableRead = 0x0220
    DataLinkTableWrite = 0x0221
    ProgAreaProtect = 0x0304
    ProgAreaProcClear = 0x0305
    ProgAreaRead = 0x0306
    ProgAreaWrite = 0x0307
    ProgAreaClear = 0x0308
    Run = 0x0401
    Stop = 0x0402
    Reset = 0x0403
    CtrDataRead = 0x0501
    ConnDataRead = 0x0502
    CtrStatRead = 0x0601
    NetStatRead = 0x0602
    DLinkStatRead = 0x0603
    CTimeRead = 0x0620
    ClockRead = 0x0701
    ClockWrite = 0x0702
    BcasTestDataSend = 0x0801
    BcastTestResultsRead = 0x0802
    MessageRead = 0x0920
    AccessRightAq = 0x0C01
    AccessRightFAq = 0x0C02
    AccessRightRel = 0x0C03
    ErrorClear = 0x2101
    ErrorLogRead = 0x2102
    ErrorLogClear = 0x2103
    FileMemIndexRead = 0x220F
    FileMemRead = 0x2210
    FileMemWrite = 0x2211
    ForceSetReset = 0x2301
    ForceSetResetCancel = 0x2302
    MulPointForceStatusRead = 0x230A
    NameSet = 0x2601
    NameDel = 0x2602
    NameRead = 0x2603
    Unknown = 0x0000

    def to_bytes(self) -> bytes:
        return self.value.to_bytes(2, "big")

    @staticmethod
    def fromBytes(data: bytes):
        try:
            return CmdBytes(data[:2])
        except ValueError:
            return CmdBytes.Unknown
