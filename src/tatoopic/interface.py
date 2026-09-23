#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from .img_processing import ImgProcessing as img

class Interface :
    AVAILABLE_CHANNELS = ("R", "G", "B", "A")

    def isImgFile(self, path : str) :
        file = Path(path)
        if file.exists() :
            return path.endswith(img.SUPPORTED_FILES)
        return False 

    def __init__(self):
        print("Hello there !")

        valid_file = False
        while not valid_file : 
            img_path = str(input("Load your image here (write the path or drag and drop): "))
            img_path = img_path.strip(" &'")

            valid_file = self.isImgFile(img_path)
            if valid_file:
                self.img_path = img_path
                self.img_processing = img(self.img_path)
            else : 
                print("This file doesn't exist or is not in a supported format. Please try again. \n")

        is_running = True
        while is_running :
            is_running = self.featureOptions()
            if (not is_running) :
                print("Goodbye ! I hope you enjoyed the app :)")

           
    
    def readImg(self) :
        try : 
            
            if (not self.img_processing.isImgBW()) :
                
                channel = ""
                while channel.upper() not in self.AVAILABLE_CHANNELS :
                    channel = str(input("In which channel do you want to read the message ? (R, G, B, A) : "))
                    if channel.upper() not in self.AVAILABLE_CHANNELS :
                        print("Invalid entry, try again")
                match channel.upper() :
                    case "R" :
                        print("Here's what's in the red channel of this image :")
                        print(self.img_processing.readInChannel(img.COLOR_CHANNEL_R))
                        
                    case "G" :
                        print("Here's what's in the green channel of this image :")
                        print(self.img_processing.readInChannel(img.COLOR_CHANNEL_G))

                    case "B" :
                        print("Here's what's in the blue channel of this image :")
                        print(self.img_processing.readInChannel(img.COLOR_CHANNEL_B))

                    case "A" :
                        print("Here's what's in the alpha channel of this image :")
                        print(self.img_processing.readInChannel(img.COLOR_CHANNEL_A))
            else :
                print("Here's what's in the channel of this image :")
                print(self.img_processing.readInChannel())
        except Exception as error:
            for e in error.args :
                print("Whoops ! ", e)

    def writeImg(self) :
        message = str(input("What do you want to write in this image ? : "))
        try :
            if (not self.img_processing.isImgBW()) :
                channel = ""
                while channel.upper() not in self.AVAILABLE_CHANNELS :
                    channel = str(input("In which channel do you want to write the message ? (R, G, B, A) : "))
                    if channel.upper() not in self.AVAILABLE_CHANNELS :
                        print("Invalid entry, try again")
                match channel.upper() :
                    case "R" :
                        print("Tatooing in the red channel of this image...")
                        print("Saved in path : ", self.img_processing.writeInChannel(message, img.COLOR_CHANNEL_R))
                        
                    case "G" :
                        print("Tatooing in the green channel of this image...")
                        print("Saved in path : ", self.img_processing.writeInChannel(message, img.COLOR_CHANNEL_G))

                    case "B" :
                        print("Tatooing in the blue channel of this image...")
                        print("Saved in path : ", self.img_processing.writeInChannel(message, img.COLOR_CHANNEL_B))

                    case "A" :
                        print("Tatooing in the alpha channel of this image...")
                        print("Saved in path : ", self.img_processing.writeInChannel(message, img.COLOR_CHANNEL_A))
            else :
                print("Tatooing in the channel of this image...")
                print("Saved in path : ", self.img_processing.writeInChannel(message))
        except Exception as error:
            for e in error.args :
                print("Whoops ! ", e)
        


    def featureOptions(self) :
        print("What do you want to do with this image ?")
        choice = str(input("R for reading, W for writing, Q to quit : "))
        match choice.upper():
            case "R" :
                self.readImg()
            case "W" :
                self.writeImg()
            case "Q" :
                return False
            case _ :
                print("Invalid entry, try again")
        print("")
        return True
        
        
