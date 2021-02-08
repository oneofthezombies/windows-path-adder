from typing import List


class TryDecodeError(Exception):
    def __init__(self, byte_string: bytes, encodings: List[str]):
        super().__init__(f'[{byte_string}] decoding failed. tried encodings: [{encodings}]')
        self.byte_string = byte_string
        self.encodings = encodings


class NotSupportError(Exception):
    def __init__(self, platform: str):
        super().__init__(f'current platform is not supported. [{platform}]')
        self.platform = platform
