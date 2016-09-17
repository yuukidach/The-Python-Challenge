#! /usr/bin/env python3
# -*- coding: utf-8 -*-

code = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dm"
        "p. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq "
        "qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc"
        " spj.")

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
transtab = "".maketrans(intab,outtab)

print(code.translate(transtab))
