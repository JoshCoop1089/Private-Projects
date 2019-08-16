# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:44:25 2017

@author: Josh
"""

s='asjdhskbobajfhasvbob'
#find all 'bc'#

bob=0
q=1
r=1
for x in s:
    if x == 'b':
        w=s[int(q):int(q)+1]
        print ("w is now: " +w)
        q+=1
        r+=1
        for z in w:
            if z == 'o':
                a=s[int(r):int(r)+1]
                print ("a is now: " +a)
                for c in a:
                    if c == "b":
                        bob +=1
                        print(bob)
                        break
    else:
        q+=1
        r+=1
print ('Final Count of bob is: '+ str(bob))
