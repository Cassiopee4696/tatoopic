#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2 as cv

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
        print("ASCII : ", ascii_value)
        octet = ""
        while ascii_value > 0 :
            bit = ascii_value % 2
            ascii_value = ascii_value // 2
            caracter_bytes.append(bit)
            octet += str(bit)
        
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