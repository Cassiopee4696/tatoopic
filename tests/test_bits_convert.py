#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.tatoopic.bits_convert import BitsConvert as b 

def test_intToBit() :
    assert b.intToBit(122) == 0
    assert b.intToBit(157) == 1

def test_bytesToInt() :
    bytes_array = [0,1,0,1,0,0,0,0]
    assert b.bytesToInt(bytes_array) == 10

def test_intToBytes() :
    assert b.intToBytes(127) == [1,1,1,1,1,1,1,0]

