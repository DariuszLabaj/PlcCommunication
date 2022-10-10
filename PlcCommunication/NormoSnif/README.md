# Omron FINS protocol based on W227E12: FINS Commands Reference Manual
## To create, validate and parse frames, create plc freame factory object
```py
import PlcCommunication.NormoSnif as Fins
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
print(generatedFrame)
bytesToSend = generatedFrame.data
expectedReplySize = generatedFrame.replyFrameSize

receivedData = dataTransmision(bytesToSend, expectedReplySize)
print(f'{" | ".join(f"{v:02x}" for v in receivedData[:14])}')
errorData, frameData = frameFactory.validateFrames(bytesToSend, receivedData)
print(frameData[:frameData.find(b'\x00')].decode('ascii'))
```

Output:

    80 | 00 | 02 | 00 | ff | 00 | 00 | 7e | 00 | 01 | 05 | 01
    c0 | 00 | 02 | 00 | 7e | 00 | 00 | ff | 00 | 01 | 05 | 01 | 00 | 40
    NX102-1020          1.38.00

## Reading from memory space
To read form memory space that memory space need to be enable on plc side then with correct PLC you can just ask for data in that memory designation

```py
generatedFrame = frameFactory.MemoryAreaRead(
    areaCode=Fins.Nx1.MemDesignation.CIO, beginningAddress=0, noOfITems=1000
)
print(generatedFrame)
bytesToSend = generatedFrame.data
expectedReplySize = generatedFrame.replyFrameSize

receivedData = dataTransmision(bytesToSend, expectedReplySize)
print(f'{" | ".join(f"{v:02x}" for v in receivedData[:14])}')
```

Output:

    80 | 00 | 02 | 00 | ff | 00 | 00 | 7e | 00 | 02 | 01 | 01 | b0 | 00 | 00 | 00 | 03 | e8
    c0 | 00 | 02 | 00 | 7e | 00 | 00 | ff | 00 | 02 | 01 | 01 | 00 | 40

## Validate Data before parsing
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
    wordIndex = 0
    value: float = Fins.DataConversion.from_real(data=frameData, poz=wordIndex)
    print(errorData.text)
    print(value)
```

Output:

    PLC Non Fatal Error Normal Comlpetion : ---
    1.401298464324817e-45