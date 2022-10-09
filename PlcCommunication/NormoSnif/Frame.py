from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Frame:
    data: bytearray

    @property
    def length(self):
        return len(self.data)

    def __str__(self):
        return ' | '.join([f'{byte:02x}' for byte in self.data])


@dataclass(slots=True, frozen=True)
class CommandFrame(Frame):
    data: bytearray
    replyFrameSize: int

    @property
    def length(self):
        return len(self.data)

    def __str__(self):
        return ' | '.join([f'{byte:02x}' for byte in self.data])

    def __repr__(self):
        return ' | '.join([f'{byte:02x}' for byte in self.data])
