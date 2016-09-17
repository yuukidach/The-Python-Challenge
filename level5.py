#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yuuki_Dach'

from urllib import request
import pickle

pyUrl = 'http://www.pythonchallenge.com/pc/def/banner.p'
req = request.Request(pyUrl)
resp = request.urlopen(req)
urlContent = resp.read()
code = []
pic = pickle.loads(urlContent)
for line in pic:
    for letter, num in line:
        code.append(num*letter)
    code.append('\n')
print("".join(code))
