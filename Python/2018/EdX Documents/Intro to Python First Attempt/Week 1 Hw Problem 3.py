# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 00:29:35 2017

@author: Josh
"""
#bugs: 
#last letter bugs, doesn't look for new strings after finding 
#the first backward facing string, doesn't reverse certain strings properly
s='abcdeffdefghhjyt' #should give answer of 'drw'






i=1
j=0
str1=''
str2=''
while i<len(s) and j<len(s):
    if s[i]<s[i-1]:
        if str1!='':
            str2+=s[j:i]
            print('str2 is now: ' +str(str2))
            if len(str2)>len(str1):
                str1=str2
                str2=''
            else:
                str2=''
        else:
            str1+=s[j:i]
        print('str1 is now: ' +str(str1))
        j=i
        print('j is now: ' +str(j))
        i+=1
    elif s[i]==s[i-1] or s[i]>s[i-1]:
        i+=1
if s[len(s)-1]>s[len(s)-2] or s[len(s)-1]==s[len(s)-2]: #last term alphabetic
    if len(s[j:])>len(str1):
        str1=s[j:]                                          #for last string
if str1=='':             #full alphabetic catch
    str1=s
print ('Longest substring in alphabetical order is: '+ str(str1))
