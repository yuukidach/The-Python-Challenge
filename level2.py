#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yuuki_Dach'

from urllib import request
import re

pyUrl = "http://www.pythonchallenge.com/pc/def/ocr.html"
req = request.Request(pyUrl)
resq = request.urlopen(req)
content = resq.read()
book = re.compile(b"<!--(.*?)-->", re.S)
bookContents = re.findall(book, content)
wordsCmpl = re.compile(b"([ a-zA-Z])", re.S)
for bookContent in bookContents: 
    words = re.findall(wordsCmpl, bookContent)
    code = ""
    for word in words:
        code += word.decode("ascii")
    print(code)
