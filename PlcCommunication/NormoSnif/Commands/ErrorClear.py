from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ErrorClear(failNo: int) -> bytes:
    """
    Clears errors from the PC. A normal response will be returned even if an error has not occurred\nFFFE Present
    error cleared. Resets the highest priority error.\n0002 Power interruption error. This error occurs when the CPU
    power has been interrupted.\n00A0 to 00A7 SYSMAC BUS error\n00B0 to 00B3 SYSMAC BUS/2 error\n00E7 I/O
    verification error. This error occurs if the I/O table differs from the actual I/O points in the System.\n00F4
    Non-fatal SFC error. This error occurs when there is an error while the PC is executing an SFC program.\n00F7
    Battery error\n00F8 Indirect DM error. This error occurs when a mistake has occurred in indirectly addressing
    the DM Area.\n00F9 JMP error. This error occurs when a jump has been specified without a destination.\n0200 to
    0215 CPU Bus Unit error (the rightmost two digits are the unit number in BCD of the Unit that has the error).
    This error occurs if there is a parity error at the time of data transfer between the CPU Bus Unit and CPU or
    if the CPU Bus Unit has a watchdog timer error.\n0400 to 0415 CPU Bus Unit setting error (the rightmost two
    digits are the unit number in BCD of the Unit that has the error).\n4101 to 42FF FAL(006) executed in the user
    program.\nThe following codes can be used only when the PC is in PROGRAM mode\nFFFF All errors cleared.\n809F
    Cycle time too long\n80C0 to 80C7 I/O bus error. This error occurs when there is an error in an I/O bus check
    or a Unit has been removed or added when power is turned on to the PC.\n80E0 I/O setting error. This error
    occurs if the I/O table differs from actual I/O points in the System. \n80E1 I/O points overflow \n80E9
    Duplication error. This error occurs if the same unit number is assigned more than one Unit or the same word
    is allocated more than once.\n80F0 Program error. This error occurs if a program that exceeds memory capacity
    is executed. \n80F1 Memory error. This error occurs if an error is found in the PC’s memory, memory card, or
    PC Setup during an memory error check.\n80F3 Fatal SFC error. This error occurs if an SFC syntax error has been
    discovered and the program will not execute.\n80FF System error. This error occurs if the CPU has a watchdog
    timer error.\n8100 to 8115 CPU bus error. The rightmost two digits are the unit number in BCD of the CPU Bus
    Unit that has the error. This error occurs if an error is discovered during a CPU bus check.\nC101 to C2FF
    FALS(007) executed.\n
    """
    return CmdBytes.ErrorClear.to_bytes() + failNo.to_bytes(2, "big")
