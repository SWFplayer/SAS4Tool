import numpy as np

def hash2 (num: int) -> np.uint32:
    loc2 = np.uint32(num)
    loc4 = 3988292384
    for _ in range(8):
        loc2 = loc2.view(np.int32)
        if (loc2 & 1):
            loc2 >>= 1
            loc2 ^= loc4
        else:
            loc2 >>= 1
        loc2 = np.uint32(loc2)
    return loc2

def hash1 (buf) -> np.uint32:
    loc7 = np.uint32( 0 )
    for loc6 in range(len(buf)):
        loc2 = buf[loc6]
        loc3 = (loc7 ^ loc2) & 255
        loc7 = np.uint32( ((loc7 >> 8) & 16777215) ^ hash2(loc3) )
    if (loc7 < 0):
        loc7 = np.uint32( 4294967295 + loc7 + 1 )
    return loc7


def dgdata_decode (data: bytes) -> np.ndarray:
    nddata = np.frombuffer( data, np.uint8 )
    nddata = nddata[14:].copy()
    for i in range(len(nddata)):
        nddata[i] -= 21
        nddata[i] -= i % 6
    return nddata


def dgdata_encode (data: bytes) -> np.ndarray:
    e_data = np.frombuffer( data, np.uint8 ).copy()
    e_header = np.frombuffer( f'DGDATA{hash1(e_data):08x}'.encode('utf-8'), np.uint8 )
    for i in range(len(e_data)):
        e_data[i] += i % 6
        e_data[i] += 21
    return np.concatenate( (e_header,e_data,) )