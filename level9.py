#! /usr/bin/env python3
# -*- coding: utf-8 -8-
__author__ = 'Yuuki_Dach'

import requests
import re
from PIL import Image, ImageDraw

webUrl = 'http://www.pythonchallenge.com/pc/return/good.html'
webContent = requests.get(webUrl, auth=('huge','file')).text
print(webContent)
pattern = re.compile(r"(\d{2,3})")
nums = re.findall(pattern, webContent)
nums = list(map(int,nums))
nums.remove(nums[0])
nums.remove(nums[0])
print(nums)
img = Image.new('RGB', (800,800))
draw = ImageDraw.Draw(img)
draw.polygon(nums, 'white')
img.show()

