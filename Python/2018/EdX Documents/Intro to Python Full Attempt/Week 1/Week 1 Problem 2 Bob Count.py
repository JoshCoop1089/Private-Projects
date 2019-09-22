# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:11:29 2018

@author: joshc
"""

s='azcbobobegghakl'
i=0
bobcount=0
while i<(len(s)-2):
    print('Checking group: ' +str(s[i:i+3]))
    if s[i:i+3]=='bob':
        bobcount +=1
        print(bobcount)
        i+=1
        if bobcount>5:
            print('you fucked up')
            break
        print('i count is: ' +str(i))
    else:
        i+=1
        print('i count is: '+str(i))
print("Number of times bob occurs is: " +str(bobcount))