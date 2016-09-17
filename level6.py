#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yuuki_Dach'

import zipfile
import re

zipFileName= 'channel.zip'
zipBag = zipfile.ZipFile(zipFileName)
num = '90052'
comment = ''
while True:
    zipContent = zipBag.read(num+'.txt').decode('utf-8')
    print(zipContent)
    comment += zipBag.getinfo(num+'.txt').comment.decode('utf-8')
    content = re.search("(\d+)", zipContent)
    if content == None:
        break
    num = content.group()
print(comment)
