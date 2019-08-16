# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 23:10:24 2018

@author: joshc
"""

def timeConversion(s):
    snew=int(s[0:2])
    if 'PM' in s:
        if snew==12:
            snew=0
        pms=snew+12
        sout=str(pms)+s[2:-2]
    elif 'AM' in s:
        sout=str(snew)+s[2:-2]
        if snew<10:
            sout='0'+str(snew)+s[2:-2]
        if snew==12:
            sout='00'+s[2:-2]
    return sout
        
s='09:00:00PM'
print(timeConversion(s))