import PlcCommunication.NormoSnif as Fins
import socket


def main():
    def dataTransmision(data: bytearray, rcv_size: int) -> bytes:
        connection.send(data)
        bytes_received = connection.recv(rcv_size)
        return bytes_received

    # connect to plc

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.settimeout(0.1)
    connection.connect(("192.168.250.1", 9600))

    frameFactory = Fins.Nx1()

    # Read controller information data

    generatedFrame = frameFactory.ControllerDataRead()
    bytesToSend = generatedFrame.data
    expectedReplySize = generatedFrame.replyFrameSize

    receivedData = dataTransmision(bytesToSend, expectedReplySize)

    # Read controller memory data

    generatedFrame = frameFactory.MemoryAreaRead(
        areaCode=Fins.Nx1.MemDesignation.CIO, beginningAddress=0, noOfITems=1000
    )
    bytesToSend = generatedFrame.data
    expectedReplySize = generatedFrame.replyFrameSize

    receivedData = dataTransmision(bytesToSend, expectedReplySize)

    # validate Data befor parsing

    errorData, frameData = frameFactory.validateFrames(bytesToSend, receivedData)
    if errorData.code != 0:
        raise Fins.CommunicationErrorException(f"{errorData.text}")
    if len(receivedData) != expectedReplySize:
        raise Fins.CommunicationErrorException(
            f"Received less data then expected: {expectedReplySize = }, {len(receivedData) = }"
        )

    # parse validated Data
    wordIndex = 0
    value: float = Fins.DataConversion.from_real(data=frameData[2:], poz=wordIndex)
    print(value)


if __name__ == "__main__":
    main()
