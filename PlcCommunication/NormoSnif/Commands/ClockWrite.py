from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes
from PlcCommunication.NormoSnif import dataTypes as dt
from datetime import datetime


def ClockWrite(sourceDate: datetime) -> bytes:
    """
    Sets the clock
    Year, month, date, hour, minute, second, day (command):\n
    Each specified value is expressed in BCD.\n
    Year: The rightmost two digits of the year.\n
    Hour: Specify 00 to 23.\n
    Day: As follows:\n
    0 - Sun, 1 - Mon, 2 - Tue, 3 - Wed, 4 - Thur, 5 - Fri, 6 - Sat
    """
    commandData = CmdBytes.ClockWrite.to_bytes()
    year = (
        sourceDate.year - int(sourceDate.year / 100) * 100
        if sourceDate.year > 99
        else sourceDate.year
    )
    commandData += dt.to_bcd(year).to_bytes(1, "big")
    commandData += dt.to_bcd(sourceDate.month).to_bytes(1, "big")
    commandData += dt.to_bcd(sourceDate.day).to_bytes(1, "big")
    commandData += dt.to_bcd(sourceDate.hour).to_bytes(1, "big")
    commandData += dt.to_bcd(sourceDate.minute).to_bytes(1, "big")
    commandData += dt.to_bcd(sourceDate.second).to_bytes(1, "big")
    day = sourceDate.weekday() + 1 if sourceDate.weekday() < 6 else 0
    commandData += dt.to_bcd(day).to_bytes(1, "big")
    return commandData
