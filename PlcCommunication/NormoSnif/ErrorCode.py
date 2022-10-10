from __future__ import annotations
from dataclasses import dataclass

Normal_Comlpetion = {0x00: "---", 0x01: "Service was interrupted"}
Local_node_error = {
    0x01: "Local node not part of Network",
    0x02: "Token time-out, node number too large",
    0x03: "Number of transmit retries exceeded",
    0x04: "Maximum number of frames exceeded",
    0x05: "Node number setting error(range)",
    0x06: "Node number duplication error",
}
Destination_node_error = {
    0x01: "Destination node not part of Network",
    0x02: "No node with the specified node number",
    0x03: "Third node not part of Network | Broadcasting was specified",
    0x04: "Bussy error, destination node busy",
    0x05: "Response time-out, message packet was corrupted by noise | Response time-out, response watchdog timer interval to short | Frame lost in transmission",  # noqa: 501
}
Communications_controller_error = {
    0x01: "Error occured in the communications controller, ERC indicator is lit",
    0x02: "CPU error occured in the PC at the destination node",
    0x03: "A controller error has prevented a normal response from being returned",
    0x04: "Node number setting error",
}
Not_Executable = {
    0x01: "An undefined command has been used",
    0x02: "Cannot process command because the specified unit model or version is wrong",
}
Routing_error = {
    0x01: "Destination node number is not set in the routing table",
    0x02: "Routing table isn't registered",
    0x03: "Routing table error",
    0x04: "The maximum number of relay nodes(2) was exceeded in the command",
}
Command_format_error = {
    0x01: "The command is longer then the max permissible length",
    0x02: "The command is shorter than min. permissible length",
    0x03: "The desired number of data items differs from the actual number",
    0x04: "An incorrect command format has been used",
    0x05: "An incorrect header has been used. (the loacl node's relay table or relay node's local network table is wrong)",  # noqa: 501
}
Parameter_error = {
    0x01: "A correct memory area code has not been used or Expansion Data Memory is not available",
    0x02: "The access size specified in the command is wrong, or the firs address is an odd number",
    0x03: "The first address is in a inaccessible area",
    0x04: "The end of specified word range exceeds the acceptable range",
    0x06: "A non-existent program no. has been specified",
    0x09: "The sizes of data items in the command block are wrong",
    0x0A: "The IOM break function cannot be executed because it is already been executed",
    0x0B: "The response block is longer than the max. permissible length",
    0x0C: "An incorrect parameter code has been specified",
}
Read_not_possible = {
    0x02: "The data is protected | An attempt was made to download a file that is being uploaded",
    0x03: "The registered table does not exist or is incorrect | Too many files open",
    0x04: "The corresponding search data does not exist",
    0x05: "A non-existing program no. has been specified",
    0x06: "A non-existing file has been specified",
    0x07: "A verification error has occured",
}
Write_not_possible = {
    0x01: "The specified area is read-only or is write-protected",
    0x02: "The data is protected | An attempt was made to simultaneously download and upload a file | The data link table cannot be writen manual because it is set for automatic generation",  # noqa: 501
    0x03: "The number of files exceeds the maximum permissible | Too many files open",
    0x05: "A non-existent program no. has been specified",
    0x06: "A non-existent file has been specified",
    0x07: "The specified file already exists",
    0x08: "Data connot be changed",
}
Not_executable_in_current_mode = {
    0x01: "The mode is wrong (executing) | Data links are active",
    0x02: "The mode is wrong (stopped) | Data links are active",
    0x03: "The PC is in the PROGRAM mode",
    0x04: "The PC is in the DEBUG mode",
    0x05: "The PC is in the MONITOR mode",
    0x06: "The PC is in the RUN mode",
    0x07: "The specified node is not the control node",
    0x08: "The mode is wrong and the step cannot be executed",
}
No_Unit = {
    0x01: "A file device does not exist where specified",
    0x02: "The specified memory does not exist",
    0x03: "No clock exists",
}
Start_Stop_not_possible = {
    0x01: "The data link table either hasn't been created or is incorrect"
}
Connection_error = {0x3F: "No valid data", 0x3E: "Socket is closed"}

Unknown_error = {0xFF: "---", 0xFE: "Unable to Parse Error"}

MainErrorCodes = {
    0x00: Normal_Comlpetion,
    0x01: Local_node_error,
    0x02: Destination_node_error,
    0x03: Communications_controller_error,
    0x04: Not_Executable,
    0x05: Routing_error,
    0x10: Command_format_error,
    0x11: Parameter_error,
    0x20: Read_not_possible,
    0x21: Write_not_possible,
    0x22: Not_executable_in_current_mode,
    0x23: No_Unit,
    0x24: Start_Stop_not_possible,
    0x7F: Connection_error,
    0xFF: Unknown_error,
}

MainErrorNames = {
    0x00: "Normal_Comlpetion",
    0x01: "Local_node_error",
    0x02: "Destination_node_error",
    0x03: "Communications_controller_error",
    0x04: "Not_Executable",
    0x05: "Routing_error",
    0x10: "Command_format_error",
    0x11: "Parameter_error",
    0x20: "Read_not_possible",
    0x21: "Write_not_possible",
    0x22: "Not_executable_in_current_mode",
    0x23: "No_Unit",
    0x24: "Start_Stop_not_possible",
    0x7F: "Connection_error",
    0xFF: "Unknown_error",
}


def LookupErrorText(data: bytes) -> str:
    try:
        mainText = MainErrorNames[data[0]]
        subText = MainErrorCodes[data[0]][data[1]]
    except KeyError:
        mainText = MainErrorNames[0xFF]
        subText = MainErrorCodes[0xFF][0xFE]
    finally:
        return f"{mainText.replace('_', ' ')} : {subText}"


@dataclass(slots=True, frozen=True)
class ErrorCode:
    code: int
    text: str
    relayError: bool
    plcFatalError: bool
    plcNonFatalError: bool

    @staticmethod
    def from_bytes(data: bytes) -> ErrorCode:
        if not data or len(data) < 2:
            errorCode = bytes(bytearray([0xFF, 0xFF]))
            return ErrorCode(
                int.from_bytes(errorCode, "big", signed=False),
                LookupErrorText(errorCode), False, False, False
            )
        try:
            relayError = ''
            plcFatalError = ''
            plcNonFatalError = ''
            mainError = int.from_bytes(
                data[0:1], byteorder="big", signed=False)
            subError = int.from_bytes(data[1:2], byteorder="big", signed=False)
            if mainError & 0b1000_0000 == 0b1000_0000:
                relayError = 'Relay Error '
                mainError &= 0b0111_1111
            if subError & 0b1000_0000 == 0b1000_0000:
                plcFatalError = 'PLC Fatal Error '
                subError &= 0b0111_1111
            if subError & 0b0100_0000 == 0b0100_0000:
                plcNonFatalError = 'PLC Non Fatal Error '
                subError &= 0b1011_1111
            errorCode = bytes(bytearray([mainError, subError]))
            return ErrorCode(
                int.from_bytes(errorCode, "big", signed=False),
                f'{relayError}{plcFatalError}{plcNonFatalError}{LookupErrorText(errorCode)}',
                relayError != '', plcFatalError != '', plcNonFatalError != ''
            )
        except ValueError:
            return ErrorCode(
                int.from_bytes(errorCode, "big", signed=False),
                LookupErrorText(errorCode),
            )

    def __str__(self):
        return f"{self.code:04x} : {self.text}"
