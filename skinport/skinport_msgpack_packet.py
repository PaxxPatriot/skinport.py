"""
MIT License

Copyright (c) 2022-present PaxxPatriot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import struct

import msgpack
from msgpack import ExtType, Timestamp
from socketio.msgpack_packet import MsgPackPacket

__all__ = ("SkinportMsgPackPacket",)


class SkinportMsgPackPacket(MsgPackPacket):

    def encode(self):
        """Encode the packet for transmission."""
        return msgpack.dumps(self._to_dict(), default=self._default)

    def decode(self, encoded_packet):
        """Decode a transmitted package."""
        decoded = msgpack.loads(encoded_packet, ext_hook=self._ext_hook)
        self.packet_type = decoded['type']
        self.data = decoded.get('data')
        self.id = decoded.get('id')
        self.namespace = decoded['nsp']

    def _ext_hook(self, code, data):
        if code == 0 and len(data) == 8:
            return self._decode_timestamp_from_ext(code, data)
        return ExtType(code, data)

    @staticmethod
    def _decode_timestamp_from_ext(code, data):
        milliseconds = struct.unpack("!Q", data)[0]
        return Timestamp.from_unix(milliseconds / 1000)

    def _default(self, obj):
        if isinstance(obj, Timestamp):
            return self._encode_timestamp_to_ext(obj)
        return obj

    @staticmethod
    def _encode_timestamp_to_ext(obj):
        milliseconds = int(obj.to_unix() * 1000)
        return ExtType(0, struct.pack("!Q", milliseconds))
