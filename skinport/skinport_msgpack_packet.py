import struct

import msgpack
from msgpack import Timestamp, ExtType
from socketio.msgpack_packet import MsgPackPacket


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

