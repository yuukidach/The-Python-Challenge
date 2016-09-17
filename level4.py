#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yuuki_Dach'

from urllib import request
import re

mainUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
subUrl = '8022' # first try is '12345'
subUrl2 = '' 
i = 400
while subUrl != subUrl2:
    subUrl2 = subUrl
    pyUrl = mainUrl + subUrl
    req = request.Request(pyUrl)
    resp = request.urlopen(req)
    urlContent = resp.read()
    pattern = re.compile(b'\d+', re.S)
    contents = re.findall(pattern, urlContent)
    for content in contents:
        subUrl = content.decode("ascii")
    print(subUrl)
