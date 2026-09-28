#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from src.tatoopic.img_processing import ImgProcessing as img

test_img = img("./tests/img/test.png")
test_img_alpha = img("./tests/img/test_alpha.png")
test_img_BW = img("./tests/img/test_BW.png", isBW = True)

def test_isImgBW() :
    assert test_img.isImgBW() == False
    assert test_img_alpha.isImgBW() == False
    assert test_img_BW.isImgBW()== True

def test_getImgChannel() :
        test_img_channels ={ 
            "R" : test_img.getImgChannel(img.COLOR_CHANNEL_R),
            "G" : test_img.getImgChannel(img.COLOR_CHANNEL_G),
            "B" : test_img.getImgChannel(img.COLOR_CHANNEL_B),
        }
        test_img_alpha_channels = {
            "R" : test_img_alpha.getImgChannel(img.COLOR_CHANNEL_R),
            "G" : test_img_alpha.getImgChannel(img.COLOR_CHANNEL_G),
            "B" : test_img_alpha.getImgChannel(img.COLOR_CHANNEL_B),
            "A" : test_img_alpha.getImgChannel(img.COLOR_CHANNEL_A)
        }
        
        test_img_BW_channel = {
            "BW" : test_img_BW.getImgChannel()
        }

        assert test_img_channels["R"][0][0] == 104
        assert test_img_channels["G"][0][0] == 187
        assert test_img_channels["B"][0][0] == 213
        
        assert test_img_alpha_channels["R"][70][50] == 55
        assert test_img_alpha_channels["G"][70][50] == 143
        assert test_img_alpha_channels["B"][70][50] == 171
        assert test_img_alpha_channels["A"][70][50] == 164 
                  
        assert test_img_BW_channel["BW"][0][0] == 175 

def test_readInChannel() :
    test_img_channels ={ 
        "R" : test_img.readInChannel(img.COLOR_CHANNEL_R),
        "G" : test_img.readInChannel(img.COLOR_CHANNEL_G),
        "B" : test_img.readInChannel(img.COLOR_CHANNEL_B),
    }
    test_img_alpha_channels = {
        "R" : test_img_alpha.readInChannel(img.COLOR_CHANNEL_R),
        "G" : test_img_alpha.readInChannel(img.COLOR_CHANNEL_G),
        "B" : test_img_alpha.readInChannel(img.COLOR_CHANNEL_B),
        "A" : test_img_alpha.readInChannel(img.COLOR_CHANNEL_A)
    }
    
    test_img_BW_channel = {
        "BW" : test_img_BW.readInChannel()
    } 

    assert test_img_channels["R"][0] == "\x00"
    assert test_img_channels["G"][0] == "ÿ"
    assert test_img_channels["B"][0] == "ÿ"

    assert test_img_alpha_channels["R"][0] == "\x00"
    assert test_img_alpha_channels["G"][0] == "\x00"
    assert test_img_alpha_channels["B"][0] == "\x00"
    assert test_img_alpha_channels["A"][0] == "\x00"

    assert test_img_BW_channel["BW"][0] == "ÿ"

def test_writeInChannel() :
    message = "Hello World !"
    
    output_img = test_img.writeInChannel(message, img.COLOR_CHANNEL_R)
    output_img_alpha = test_img_alpha.writeInChannel(message, img.COLOR_CHANNEL_R)
    output_img_BW = test_img_BW.writeInChannel(message)
    
    assert os.path.exists(output_img)
    assert os.path.exists(output_img_alpha)
    assert os.path.exists(output_img_BW)

    test_output_img = img(output_img)
    test_output_img_alpha = img(output_img_alpha)
    test_output_img_BW = img(output_img_BW)

    assert message in test_output_img.readInChannel(img.COLOR_CHANNEL_R)
    assert message in test_output_img_alpha.readInChannel(img.COLOR_CHANNEL_R)
    assert message in test_output_img_BW.readInChannel(img.COLOR_CHANNEL_R)

    os.remove(output_img)
    os.remove(output_img_alpha)
    os.remove(output_img_BW)









