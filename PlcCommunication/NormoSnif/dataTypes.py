#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8

# --Module Import--
import struct
from typing import List


def BITO(bits, source) -> List[bool]:
    '''Moves a number of binary bits from number or register to flags,\n
    Bits - is the number of bits to transfer\n
    Source - is the source number\n
    Dest - is destiantion array\n
    Author: Dariusz Łabaj
    '''
    ret = [None]*bits
    for i in range(0, int(bits)):
        if (source >> i) & 1:
            ret[i] = True
        else:
            ret[i] = False
    return ret


def BITI(bits, source) -> int:
    '''Moves a number of binary bits from input or flags arry to number or register,\n
    Bits - is the number of bits to transfer\n
    Source - is the bit array\n
    Dest - is destination register\n
    Author: Dariusz Łabaj
    '''
    dest = 0
    for i in range(0, bits):
        dest += int(source[i])*(2**(i))
    return dest


def from_int(data, poz):
    poz = poz*2
    return struct.unpack('>h', data[poz:poz + 2])[0]


def to_int(data):
    return bytearray(struct.pack(">h", data))


def from_dint(data, poz):
    poz = poz * 2
    return struct.unpack('>i', bytearray([data[poz+2], data[poz+3], data[poz+0], data[poz+1]]))[0]


def to_dint(data):
    _temp_bytes = bytearray(struct.pack(">i", data))
    return bytearray([_temp_bytes[2], _temp_bytes[3], _temp_bytes[0], _temp_bytes[1]])


def from_uint(data, poz):
    poz = poz * 2
    return struct.unpack('>H', data[poz:poz + 2])[0]


def to_uint(data):
    return bytearray(struct.pack(">H", data))


def from_udint(data, poz):
    poz = poz * 2
    return struct.unpack('>I', bytearray([data[poz + 2], data[poz + 3], data[poz], data[poz + 1]]))[0]


def to_udint(data):
    _temp_bytes = bytearray(struct.pack(">I", data))
    return bytearray([_temp_bytes[2], _temp_bytes[3], _temp_bytes[0], _temp_bytes[1]])


def from_real(data, poz) -> float:
    poz = poz * 2
    return struct.unpack('>f', bytearray([data[poz + 2], data[poz + 3], data[poz], data[poz + 1]]))[0]


def to_real(data):
    _temp_bytes = bytearray(struct.pack(">f", data))
    return bytearray([_temp_bytes[2], _temp_bytes[3], _temp_bytes[0], _temp_bytes[1]])


def from_lreal(data, poz) -> float:
    poz = poz * 2
    return struct.unpack('>d', bytearray([data[poz + 6], data[poz + 7], data[poz + 4], data[poz + 5], data[poz + 2],
                                          data[poz + 3], data[poz], data[poz + 1]]))[0]


def to_lreal(data):
    _temp_bytes = bytearray(struct.pack(">d", data))
    return bytearray(
        [
            _temp_bytes[6], _temp_bytes[7], _temp_bytes[4], _temp_bytes[5],
            _temp_bytes[2], _temp_bytes[3], _temp_bytes[0], _temp_bytes[1]])


def from_lint(data, poz):
    poz = poz * 2
    return struct.unpack('>q', bytearray([data[poz + 6], data[poz + 7], data[poz + 4], data[poz + 5], data[poz + 2],
                                          data[poz + 3], data[poz], data[poz + 1]]))[0]


def to_lint(data):
    _temp_bytes = bytearray(struct.pack(">q", data))
    return bytearray(
        [
            _temp_bytes[6], _temp_bytes[7], _temp_bytes[4], _temp_bytes[5],
            _temp_bytes[2], _temp_bytes[3], _temp_bytes[0], _temp_bytes[1]])


def from_ulint(data, poz):
    poz = poz * 2
    return struct.unpack('>Q', bytearray([data[poz + 6], data[poz + 7], data[poz + 4], data[poz + 5], data[poz + 2],
                                          data[poz + 3], data[poz], data[poz + 1]]))[0]


def to_ulint(data):
    _temp_bytes = bytearray(struct.pack(">Q", data))
    return bytearray(
        [
            _temp_bytes[6], _temp_bytes[7], _temp_bytes[4], _temp_bytes[5],
            _temp_bytes[2], _temp_bytes[3], _temp_bytes[0], _temp_bytes[1]])


def from_sint(data, poz):
    poz = poz * 2
    return struct.unpack('>b', data[poz+1:poz+2])[0]


def from_usint(data, poz):
    poz = poz * 2
    return struct.unpack('>B', data[poz+1:poz+2])[0]


def from_string(data, poz, length):
    poz = poz * 2
    newdata = swapBytes(data[poz: poz+length])
    newdata = newdata[:newdata.find(b'\x00')]
    return newdata.decode('ascii')


def to_string(data: str, size: int) -> bytes:
    bytedata = data.encode('ascii')
    if len(bytedata) % 2 != 0:
        bytedata += b'\x00'
    sbyteData = swapBytes(bytedata)
    sbyteData += b'\x00'*(size-len(sbyteData))
    return sbyteData


def swapBytes(source: bytes) -> bytes:
    if len(source) % 2 != 0:
        raise InvalidOperationException(
            f'Source length must be even, actual: {len(source)}')
    result: bytes = [b'\x00']*len(source)
    for i in range(0, len(source), 2):
        result[i] = (source[i+1]).to_bytes(1, 'little')
        result[i+1] = (source[i]).to_bytes(1, 'little')
    return b''.join(result)


class InvalidOperationException(Exception):
    ...


def to_bcd(number):
    """
    Calculate and return packed BCD value of variable

    :param number: int, list(int)
    :return: int, list(int)
    """
    iteration = 0
    if isinstance(number, int):
        result = 0
        while number > 0:
            quotient, remainder = divmod(number, 10)
            result += remainder << 4 * iteration
            number = quotient
            iteration += 1
    elif isinstance(number, list):
        result = []
        for num in number:
            if not isinstance(num, int):
                raise ValueError('list must contain ints')
            partial_result = 0
            while num > 0:
                quotient, remainder = divmod(num, 10)
                partial_result += remainder << 4 * iteration
                num = quotient
                iteration += 1
            result.append(partial_result)
            iteration = 0
    else:
        raise ValueError('variable type not supported')

    return result


def from_bcd(number):
    """
    Calculate and returns values from packed BCD

    :param number: int, list(int), bytes, bytearray
    :return: int, list(int)
    """
    iteration = 0
    if isinstance(number, int):
        result = 0
        while number > 0:
            quotient, remainder = divmod(number, 16)
            result += remainder * 10 ** iteration
            number = quotient
            iteration += 1
    elif isinstance(number, bytes) or isinstance(number, bytearray):
        if len(number) > 1:
            result = []
            for byte in number:
                partial_result = 0
                while byte > 0:
                    quotient, remainder = divmod(byte, 16)
                    partial_result += remainder * 10 ** iteration
                    byte = quotient
                    iteration += 1
                result.append(partial_result)
                iteration = 0
        else:
            number = int.from_bytes(number, "big", signed=False)
            result = 0
            while number > 0:
                quotient, remainder = divmod(number, 16)
                result += remainder * 10 ** iteration
                number = quotient
                iteration += 1
    elif isinstance(number, list):
        if len(number) > 1:
            result = []
            for byte in number:
                if not isinstance(byte, int):
                    raise ValueError('Listed variables must be int')
                partial_result = 0
                while byte > 0:
                    quotient, remainder = divmod(byte, 16)
                    partial_result += remainder * 10 ** iteration
                    byte = quotient
                    iteration += 1
                result.append(partial_result)
                iteration = 0
        else:
            if not isinstance(number, int):
                raise ValueError('Listed variables must be int')
            result = 0
            while number > 0:
                quotient, remainder = divmod(number, 16)
                result += remainder * 10 ** iteration
                number = quotient
                iteration += 1
    else:
        raise ValueError("Input must be int, bytes, or list of int's")

    return result
