#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yuuki_Dach'

from PIL import Image
from io import BytesIO
import requests

imgUrl = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
img = Image.open(BytesIO(requests.get(imgUrl).content))
midPixel = [img.getpixel((i,img.height>>1)) for i in range(0,img.width,7)]
code = [r for r, g, b ,a in midPixel if r==g==b]
print("".join(map(chr,code)))

nextCode = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join(map(chr,nextCode)))
