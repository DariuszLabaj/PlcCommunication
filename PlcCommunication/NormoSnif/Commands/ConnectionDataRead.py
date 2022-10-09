from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ConnectionDataRead(unitAddress: int, noOfUnits: int) -> bytes:
    """
    Reads the model number of the specified Units.\n
    Unit address (command and response): The unit address of the first Unit whose model number is to be read. If the
    specified Unit does not exist, the CONTROLLER DATA READ command is executed from the next Unit. Specify the
    following for the unit address.\n
    CPU: 00\n
    CPU Bus Unit: 10 + unit number in hexadecimal\n
    No. of Data Units (command): The number of data units for which the model number is to be read. A number between
    01 and 19 (hexadecimal) can be specified. If the number of data units is not specified, 19 (25 data units) will
    be used.\n
    No. of Units (response): The number of Units for which a model number is being returned. If bit 7 is ON (1), the
    model number of the last Unit is being returned.\n
    Unit address and model number (response): The unit address and model number. The model number is provided in up
    to 20 ASCII characters.
    """
    if noOfUnits < 1:
        raise ValueError("noOfUnits must be more then 0")
    if noOfUnits > 0x19:
        noOfUnits = 0x19
    commandData = CmdBytes.ConnDataRead.to_bytes()
    if unitAddress > 0 and unitAddress < 10:
        unitAddress = unitAddress + 0x10
    commandData += unitAddress.to_bytes(1, "big")
    commandData += noOfUnits.to_bytes(1, "big")
    return commandData
