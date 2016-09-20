#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO
from PIL import Image
__author__ = 'Yuuki_Dach'

img = Image.open('cave.jpg')
width, height = img.size
even = Image.new('RGB', (width >> 1, height >> 1))
odd = Image.new('RGB', (width >> 1, height >> 1))
for i in range(width):
    for j in range(height):
        imgPixel = img.getpixel((i, j))
        if (i + j) & 1 == 1:
            odd.putpixel((i >> 1, j >> 1), imgPixel)
        else:
            even.putpixel((i >> 1, j >> 1), imgPixel)
even.show()
odd.show()
