#!/usr/bin/python
# -*- coding: utf-8 -*-

class ChannelError(Exception) :
    def __init__(self, *args):
        super().__init__(*args)