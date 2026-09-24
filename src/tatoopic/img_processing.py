#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2 as cv
import os
from .bits_convert import BitsConvert


class ImgProcessing :
    COLOR_CHANNEL_A = 3
    COLOR_CHANNEL_R = 2
    COLOR_CHANNEL_G = 1
    COLOR_CHANNEL_B = 0
    COLOR_CHANNEL_BW = -1
    SUPPORTED_FILES = (".png", ".jpg", ".bmp")
    MAX_READING = 4000

    def __init__(self, img_path : str):
        self.__img = cv.imread(img_path)
        self.__path = img_path

    def isImgBW(self) :
        return len(self.__img[0][0]) == 1

    def getImgChannel(self, channel : int = COLOR_CHANNEL_BW) :
        try :
            if self.isImgBW() :
                return self.__img
            else :
                if len(self.__img[0][0]) == 3 and channel == ImgProcessing.COLOR_CHANNEL_A :
                    raise IndexError("No alpha channel")
                else :
                    return self.__img[:,:,channel].copy()
        except Exception :
            raise

    def saveImg(self, img_channel, channel : int = COLOR_CHANNEL_BW) :
        path, extension = os.path.splitext(self.__path)
        img_tatooed_path = path + "_tatooed.png"

        if channel == self.COLOR_CHANNEL_BW:
            img_tatooed = img_channel
        else:
            img_tatooed = self.__img.copy()
            img_tatooed[:, :, channel] = img_channel

        cv.imwrite(img_tatooed_path, img_tatooed)
        return img_tatooed_path

    def readInChannel(self, channel : int = COLOR_CHANNEL_BW) :
        try :
            img_channel = self.getImgChannel(channel)
            img_bits = []
            nb_pxl = 0
            for y in range(0, len(img_channel)) :
                if (nb_pxl == self.MAX_READING) :
                    break
                for x in range(0, len(img_channel[y])) :
                    if (nb_pxl == self.MAX_READING) :
                        break
                    pxl_bit = BitsConvert.intToBit(int(img_channel[y][x]))
                    img_bits.append(pxl_bit)
                    nb_pxl +=1

            bytes_array = []
            message = ""
            for bit in img_bits :
                bytes_array.append(bit)
                if len(bytes_array) == 8 :
                    ascii_chr = chr(BitsConvert.bytesToInt(bytes_array))
                    message += ascii_chr
                    bytes_array = []
            return message
        except Exception :
            raise

    def writeInChannel(self, message : str, channel : int = COLOR_CHANNEL_BW) :
        try: 
            img_channel = self.getImgChannel(channel)
            message_bits = []

            for chr in message :
                chr_bytes = BitsConvert.intToBytes(ord(chr))
                message_bits += chr_bytes

            nb_message_bits = len(message_bits)
            if nb_message_bits > len(img_channel) * len(img_channel) :
                raise IndexError("Not enough pixels")

            nb_pxl = 0
            for y in range(len(img_channel)) :
                for x in range(len(img_channel[y])) :
                    if nb_pxl == nb_message_bits :
                        break
                    pixel = img_channel[y][x]
                    bit = message_bits[nb_pxl]
                    if (BitsConvert.intToBit(pixel) != bit) :
                        if (pixel == 255) :
                            img_channel[y][x] = pixel - 1
                        else :
                            img_channel[y][x] = pixel + 1
                    nb_pxl +=1   
                if nb_pxl == nb_message_bits :
                    break
            return self.saveImg(img_channel, channel)
        except Exception :
            raise

"""

def imgread_message(img, max_message_size = 4000) : 
    bits = []
    for y in range(0, len(img)) :
        for x in range(0, len(img[y])) :
            bits.append(img[y][x] % 2)

    bytes_powers = [1, 2, 4, 8, 16, 32, 64, 128]
    power = 0
    message = ""
    base10_octet = 0
    for bit in bits : 
        base10_octet += bit * bytes_powers[power]
        power = power + 1
        max_message_size= max_message_size-1
        if (power > 7) :
            message += chr(base10_octet)
            power = 0
            base10_octet = 0
        if (max_message_size==0) :
            break
    return message 

def imgwrite_message(img, message) :
    img2 = img
    message_bytes = []
    #Conversion de chaque caractère en octet :
    for caracter in message :
        caracter_bytes = []
        ascii_value = ord(caracter)
        while ascii_value > 0 :
            bit = ascii_value % 2
            ascii_value = ascii_value // 2
            caracter_bytes.append(bit)
        
        if (len(caracter_bytes) < 8) :
            caracter_bytes += [0 for i in range(8 - len(caracter_bytes))]

        message_bytes += caracter_bytes

    nb_pixel = 0
    #Injection des bits dans les pixels de l'image :
    for y in range(0, len(img2)) :
        for x in range(0, len(img2[y])) :
            if (nb_pixel >= len(message_bytes)):
                break
            else :
                pixel = img2[y][x]
                bit = message_bytes[nb_pixel]
                if (pixel%2 != bit) :
                    if (pixel == 255) :
                        img2[y][x] = img2[y][x] - 1
                    img2[y][x] = img2[y][x] + 1
                nb_pixel +=1

        if (nb_pixel >= len(message_bytes)):
            break
    return img2
"""
