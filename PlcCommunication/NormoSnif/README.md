# Omron FINS protocol based on W227E12: FINS Commands Reference Manual
## To create, validate and parse frames, create plc freame factory object
```py
import PlcCommunication.NormoSnif as Fins
import socket

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.settimeout(0.1)
    connection.connect(("192.168.250.1", 9600))

    frameFactory = Fins.Nx1()
```
### Transmision helper funciton
```py
def dataTranssmision(data: bytearray, rcv_size: int) -> bytes:
    connection.send(data)
    bytes_received = connection.recv(rcv_size)
    return bytes_received
```
## Read controller information data
```py
    generatedFrame = frameFactory.ControllerDataRead()
    bytesToSend = generatedFrame.data
    expectedReplySize = generatedFrame.replyFrameSize

    receivedData = dataTransmision(bytesToSend, expectedReplySize)

    print(bytesToSend, expectedReplySize)
    print(generatedFrame)
```

Output:

    bytearray(b'\x80\x00\x02\x00\xff\x00\x00~\x00\x01\x05\x01') 172
    80 | 00 | 02 | 00 | ff | 00 | 00 | 7e | 00 | 01 | 05 | 01

## Reading from memory space
To read form memory space that memory space need to be enable on plc side then with correct PLC you can just ask for data in that memory designation

```py
    generatedFrame = frameFactory.MemoryAreaRead(
        areaCode=Fins.Nx1.MemDesignation.CIO, beginningAddress=0, noOfITems=1000
    )
    bytesToSend = generatedFrame.data
    expectedReplySize = generatedFrame.replyFrameSize

    receivedData = dataTransmision(bytesToSend, expectedReplySize)

    print(bytesToSend, expectedReplySize)
    print(generatedFrame)
```

Output:

    bytearray(b'\x80\x00\x02\x00\xff\x00\x00~\x00\x02\x01\x01\xb0\x00\x00\x00\x03\xe8') 2014
    80 | 00 | 02 | 00 | ff | 00 | 00 | 7e | 00 | 02 | 01 | 01 | b0 | 00 | 00 | 00 | 03 | e8

## Validate Data befor parsing
```py
    errorData, frameData = frameFactory.validateFrames(bytesToSend, receivedData)
    if errorData.code != 0:
        raise Fins.CommunicationErrorException(f"{errorData.text}")
    if len(receivedData) != expectedReplySize:
        raise Fins.CommunicationErrorException(
            f"Received less data then expected: {expectedReplySize = }, {len(receivedData) = }"
        )
```

## Parse validated Data

```py
    wordIndex = 16
    value: float = Fins.DataConversion.from_real(data=frameData[2:], poz=wordIndex) # remember to skip frist 2 bytes that contains error code data
```