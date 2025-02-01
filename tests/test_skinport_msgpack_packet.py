import datetime
import unittest

import msgpack

from skinport.skinport_msgpack_packet import SkinportMsgPackPacket


class SkinportMsgPackPacketTestCase(unittest.TestCase):

    def test_encode(self):
        # Given
        given_dt = datetime.datetime(2025, 2, 9, 8, 0, tzinfo=datetime.timezone.utc)
        given_timestamp = msgpack.Timestamp.from_datetime(given_dt)
        given_packet = SkinportMsgPackPacket(packet_type=2, data=given_timestamp, namespace='/')
        # When
        encoded_packet = given_packet.encode()
        # Then
        expected_encoded_packet = b'\x83\xa4type\x02\xa4data\xd6\xffg\xa8`\x80\xa3nsp\xa1/'
        self.assertEqual(expected_encoded_packet, encoded_packet)

    def test_decode(self):
        # Given
        encoded_packet = b'\x83\xa4type\x02\xa4data\xd6\xffg\xa8`\x80\xa3nsp\xa1/'
        # When
        decoded_packet = SkinportMsgPackPacket()
        decoded_packet.decode(encoded_packet)
        # Then
        expected_dt = datetime.datetime(2025, 2, 9, 8, 0, tzinfo=datetime.timezone.utc)
        self.assertEqual(2, decoded_packet.packet_type)
        self.assertEqual(expected_dt, decoded_packet.data.to_datetime())
        self.assertIsNone(decoded_packet.id)
        self.assertEqual('/', decoded_packet.namespace)

    def test_encode_and_decode_packet(self):
        # Given
        given_dt = datetime.datetime(2025, 2, 9, 8, 0, tzinfo=datetime.timezone.utc)
        given_timestamp = msgpack.Timestamp.from_datetime(given_dt)
        given_packet = SkinportMsgPackPacket(packet_type=2, data=given_timestamp, namespace='/')
        # When
        encoded_packet = given_packet.encode()
        decoded_packet = SkinportMsgPackPacket()
        decoded_packet.decode(encoded_packet)
        # Then
        self.assertEqual(given_packet._to_dict(), decoded_packet._to_dict())

    def test_default(self):
        with self.subTest('When object is not a Timestamp'):
            # Given
            given_obj = 'not a Timestamp'
            # When
            result = SkinportMsgPackPacket()._default(given_obj)
            # Then
            self.assertEqual(given_obj, result)

        with self.subTest('When object is a Timestamp'):
            # Given
            given_obj = msgpack.Timestamp(0, 0)
            # When
            result = SkinportMsgPackPacket()._default(given_obj)
            # Then
            self.assertIsInstance(result, msgpack.ExtType)

    def test_ext_hook(self):
        with self.subTest('When code is not 0 and data length is 8'):
            # Given
            given_code = 1
            given_data = b'\x00\x00\x01\x94\xe9\xb8\xf4'
            # When
            result = SkinportMsgPackPacket()._ext_hook(given_code, given_data)
            # Then
            self.assertIsInstance(result, msgpack.ExtType)
            self.assertEqual(1, result.code)
            self.assertEqual(b'\x00\x00\x01\x94\xe9\xb8\xf4', result.data)

        with self.subTest('When code is 0 and data length is not 8'):
            # Given
            given_code = 0
            given_data = b'\x00\x00\x01\x94\xe9\xb8\xf4'
            # When
            result = SkinportMsgPackPacket()._ext_hook(given_code, given_data)
            # Then
            self.assertIsInstance(result, msgpack.ExtType)
            self.assertEqual(0, result.code)
            self.assertEqual(b'\x00\x00\x01\x94\xe9\xb8\xf4', result.data)

        with self.subTest('When code is 0 and data length is 8'):
            # Given
            given_code = 0
            given_data = b'\x00\x00\x01\x94\xe9\xb8\xf4\x00'
            # When
            result = SkinportMsgPackPacket()._ext_hook(given_code, given_data)
            # Then
            self.assertIsInstance(result, msgpack.Timestamp)
            self.assertEqual(datetime.datetime(2025, 2, 9, 8, 0, tzinfo=datetime.timezone.utc), result.to_datetime())

    def test_encode_timestamp_to_ext(self):
        # Given
        given_dt = datetime.datetime(2025, 2, 9, 8, 0, tzinfo=datetime.timezone.utc)
        given_timestamp = msgpack.Timestamp.from_datetime(given_dt)
        # When
        ext_type = SkinportMsgPackPacket._encode_timestamp_to_ext(given_timestamp)
        # Then
        expected_ext_type = msgpack.ExtType(0, b'\x00\x00\x01\x94\xe9\xb8\xf4\x00')
        self.assertEqual(expected_ext_type, ext_type)

    def test_decode_timestamp_from_ext(self):
        # Given
        given_ext_type = msgpack.ExtType(0, b'\x00\x00\x01\x94\xe9\xb8\xf4\x00')
        # When
        timestamp = SkinportMsgPackPacket._decode_timestamp_from_ext(*given_ext_type)
        # Then
        expected_dt = datetime.datetime(2025, 2, 9, 8, 0, tzinfo=datetime.timezone.utc)
        self.assertEqual(expected_dt, timestamp.to_datetime())

    def test_encode_and_decode_timestamp(self):
        # Given
        given_dt = datetime.datetime(2025, 2, 9, 8, 0, tzinfo=datetime.timezone.utc)
        given_timestamp = msgpack.Timestamp.from_datetime(given_dt)
        # When
        ext_type = SkinportMsgPackPacket._encode_timestamp_to_ext(given_timestamp)
        timestamp = SkinportMsgPackPacket._decode_timestamp_from_ext(*ext_type)
        # Then
        self.assertEqual(given_dt, timestamp.to_datetime())
