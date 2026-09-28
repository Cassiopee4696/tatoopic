#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import os
from .bits_convert import BitsConvert


class ImgProcessing :
    COLOR_CHANNEL_A = 3
    COLOR_CHANNEL_R = 2
    COLOR_CHANNEL_G = 1
    COLOR_CHANNEL_B = 0
    COLOR_CHANNEL_BW = -1
    SUPPORTED_FILES = (".png", ".jpg", ".bmp")

    def __init__(self, img_path : str, isBW : bool = False):
        if (isBW) :
            self.__img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
        else :
            self.__img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
        self.__path = img_path

    def getImg(self) :
        return self.__img
    
    def getPath(self) :
        return self.__path

    def isImgBW(self) :
        return type(self.__img[0][0]) == np.uint8

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
                for x in range(0, len(img_channel[y])) :
                    pxl_bit = BitsConvert.intToBit(img_channel[y][x])
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

