#!/usr/bin/python
# -*- coding: utf-8 -*-

class BitsConvert :
    
    BYTES_POWERS = [1, 2, 4, 8, 16, 32, 64, 128]
    def __init__(self):
        pass

    """
    Returns bit from integer 
    (0 if even, 1 if odd)
    """
    def intToBit(nb : int):
        return nb % 2

    """
    Returns integer from bytes
    (array of 8 integers between 0 & 1)
    """
    def bytesToInt(bytes_array):
        power = 0
        base10_octet = 0
        for bit in bytes_array :
            base10_octet += bit * BitsConvert.BYTES_POWERS[power]
            power = power + 1
        return base10_octet

    """
    Returns bytes (array of 8 integers between 0 & 1) from integer
    (or nothing if the number is higher or equal to 256)
    """
    def intToBytes(nb : int, self):
       
        bytes_array = []
        while nb > 0 :
            bytes_array.append(self.intToBit(nb))
            nb = nb // 2
        return bytes_array
         

    

    