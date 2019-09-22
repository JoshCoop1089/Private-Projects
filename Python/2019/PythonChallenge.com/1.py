# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:43:15 2019

@author: joshc
"""

# url to stage 1 -> 274877906944.html
strs = 'abcdefghijklmnopqrstuvwxyz' 
def shifttext(shift):
    inp = input('Input text here: ')
    data = []
    for i in inp:                     #iterate over the text not some list
        if i in strs:                 # if the char is not a space ""  
            data.append(strs[(strs.index(i) + shift) % 26])    
        else:
            data.append(i)           #if space the simply append it to data
    output = ''.join(data)
    return output

print(shifttext(2))

#url to stage 2 -> ocr.html