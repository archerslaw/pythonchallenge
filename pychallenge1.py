#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
Level 1: 274877906944
URL: http://www.pythonchallenge.com/pc/def/274877906944.html
The picture and the hint imply that the encryption was done by replacing each letter by the the letter two places after it.
"""

import string

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

def trans(str):
    l = string.ascii_lowercase
    table = string.maketrans(l, l[2:]+l[:2])
    #return str.translate(table)
    return string.translate(str, table)

"""
t = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.  lmu ynnjw ml rfc spj."
def transWithoutTranslate():    #solved without translate
    out = ""
    for x in t:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            out += chr((ord(x) + 2 - ord('a')) % 26 + ord('a'))
        else:
            out += x
    return out
"""

def main():
    print "test the 'abcedefgh':", trans('abcdefgh')
    print trans(text)
    print trans('map')
    #print transWithoutTranslate()

if __name__ == '__main__':
    main()
