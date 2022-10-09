from PlcCommunication.NormoSnif import dataTypes as DataConversion
from PlcCommunication.NormoSnif.NX1FrameFactory import NX1FrameFactory as Nx1
from PlcCommunication.NormoSnif.NX1P2FrameFactory import NX1P2FrameFactory as Nx1p2


class CommunicationErrorException(Exception):
    ...


if __name__ == "__main__":
    help(DataConversion)
    help(Nx1)
    help(Nx1p2)
