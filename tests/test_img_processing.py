#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.tatoopic.img_processing import ImgProcessing

test_img = ImgProcessing("./tests/img/test.png")
test_img_alpha = ImgProcessing("./tests/img/test_alpha.png")
test_img_BW = ImgProcessing("./tests/img/test_BW.png", isBW = True)

def test_isImgBW() :
    assert test_img.isImgBW() == False
    assert test_img_alpha.isImgBW() == False
    assert test_img_BW.isImgBW()== True


