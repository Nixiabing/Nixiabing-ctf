# -*- coding: utf-8 -*-
import binascii
import struct

#\x49\x48\x44\x52\x00\x00\x01\xF4\x00\x00\x01\xA4\x08\x06\x00\x00\x00

crc32key = 0xCBD6DF8A
for i in range(0, 65535):
  height = struct.pack('>i', i)
  #CRC: CBD6DF8A
  data = '\x49\x48\x44\x52\x00\x00\x01\xF4' + height + '\x08\x06\x00\x00\x00'

  crc32result = binascii.crc32(data) & 0xffffffff

  if crc32result == crc32key:
    print ''.join(map(lambda c: "%02X" % ord(c), height))