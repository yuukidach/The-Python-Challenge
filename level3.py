#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yuuki_Dach'

from urllib import request
import re

pyUrl = 'http://www.pythonchallenge.com/pc/def/equality.html'
req = request.Request(pyUrl)
resp = request.urlopen(req)
urlContent = resp.read()
pattern = re.compile(b'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', re.S)
contents = re.findall(pattern, urlContent)
code = ''
for content in contents:
    code += content.decode("ascii")
print(code)
