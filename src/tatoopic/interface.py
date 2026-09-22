#!/usr/bin/python
# -*- coding: utf-8 -*-

from .img_processing import ImgProcessing as img

def interface() :
    print("Hello there !")
    img_path = str(input("In which image do you want to read the tatooed message ? : "))

    if (img_path != "") :
        img_processing = img(img_path)

        if (not img_processing.isImgBW()) :
            available_channels = ("R", "G", "B", "A")
            channel = ""
            while channel.upper() not in available_channels :
                channel = str(input("In which channel do you want to read the message ? (R, G, B, A) : "))
                if channel.upper() not in available_channels :
                    print("Invalid entry")
            match channel :
                case "R" :
                    print("Here's what's in the red channel of this image :")
                    print(img_processing.readInChannel(img.COLOR_CHANNEL_R))
                    
                case "G" :
                    print("Here's what's in the green channel of this image :")
                    print(img_processing.readInChannel(img.COLOR_CHANNEL_G))

                case "B" :
                    print("Here's what's in the blue channel of this image :")
                    print(img_processing.readInChannel(img.COLOR_CHANNEL_B))

                case "G" :
                    print("Here's what's in the alpha channel of this image :")
                    print(img_processing.readInChannel(img.COLOR_CHANNEL_A))
            return False
       
