#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 06:21:00 2018

@author: naiarafoster
"""
print("test")

from flask import Flask 
app =Flask(__name__)

@app.route("/")
def hello():
    return "Hello Movies"

