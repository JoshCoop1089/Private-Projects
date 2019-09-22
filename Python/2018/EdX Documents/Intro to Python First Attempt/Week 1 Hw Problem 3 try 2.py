# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:17:00 2017

@author: Josh
"""

#
s='abcdecz'
j=0; str1=''; str2=''; s=s+' '
for i in range(1,len(s)):
    if s[i]<s[i-1] and str1=='':
        str1=s[j:i];        j=i
    elif s[i]<s[i-1] and str1!='':
        str2=s[j:i];        j=i
        if len(str2)>len(str1):
            str1=str2
print ('Longest substring in alphabetical order is: '+ str(str1)) 

