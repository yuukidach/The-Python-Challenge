#! /usr/bin/env python3
# -*- coding: utf-8 -*-

code = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dm"
        "p. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq "        "qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc"        " spj.")
addr = ""

for alpha in code:
    if alpha!=' ' and alpha!='.' and alpha!='\'' and alpha!='(' and alpha!=')':
        if alpha == 'y':
            alpha = 'a'
        elif alpha == 'z':
            alpha = 'b'
        else:
            alpha = chr(ord(alpha)+2)
    addr += alpha 

print(addr)
