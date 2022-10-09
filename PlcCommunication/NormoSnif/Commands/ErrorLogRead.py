from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ErrorLogRead(beginningRecordNo: int, noOfRecords: int) -> bytes:
    """
    Reads the PC’s error log.\n
    Beginning record no. (command): The first record to be read (the first record number is 0000).\n
    Max. no. of stored records (response): The maximum number of records that can be recorded.\n
    No. of stored records (response): The number of records that have been recorded.\n
    No. of records (command and response): The number of records read.\n
    Error log data (response): The specified error log records will be returned in sequence starting from the
    beginning record number. The total number of bytes required is calculated as follows:\n
        No. of records x 10 bytes\n
    The configuration of each error record is as follows:\n
    Error code 1, 2: Refer to page 42 for error code 1 and to the relevant operation manual or installation guide
    for error code 2. Each data includes the second, minute, hour (0 to 23), date, month, and year (the rightmost
    two digits) in BCD specifying the time that the error occurred.
    """
    return (
        CmdBytes.ErrorLogRead.to_bytes()
        + beginningRecordNo.to_bytes(2, "big")
        + noOfRecords.to_bytes(2, "big")
    )
