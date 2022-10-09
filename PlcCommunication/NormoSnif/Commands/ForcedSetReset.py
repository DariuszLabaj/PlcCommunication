from typing import List
from PlcCommunication.NormoSnif.Commands.CmdBytes import CmdBytes


def ForcedSetReset(
    types: List[int], mem_area_codes: List[int], bits_flags: List[int]
) -> bytes:
    """
    Force-sets (ON) or force-resets (OFF) bits/flags or releases force-set status. Bits/flags that are forced ON or
    OFF will remain ON or OFF and cannot be written to until the forced status is released\n
    Set/Reset specification (command): The action to be taken for each bit/flag:\n0000 Force-reset (OFF)\n0001
    Force-set (ON)\n8000 Forced status released and bit turned OFF (0)\n8001 Forced status released and bit turned
    ON (1)\nFFFF Forced status released
    """
    if len(mem_area_codes) < len(bits_flags):
        bits_flags = bits_flags[: len(mem_area_codes)]
    if len(bits_flags) < len(mem_area_codes):
        mem_area_codes = mem_area_codes[: len(bits_flags)]
    if len(types) < len(bits_flags):
        for i in range(len(bits_flags) - len(types)):
            types.append(0xFFFF)
    if len(bits_flags) < len(types):
        types = types[: len(bits_flags)]

    commandData = CmdBytes.ForceSetReset.to_bytes()
    commandData += len(mem_area_codes).to_bytes(2, "big")
    for i in range(len(bits_flags)):
        commandData += types[i].to_bytes(2, "big")
        commandData += mem_area_codes[i].to_bytes(1, "big")
        commandData += bits_flags[i].to_bytes(3, "big")
    return commandData
