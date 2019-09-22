# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:24:45 2018

@author: joshc
"""

balance = 47730
annualInterestRate = 0.2
mIR=annualInterestRate/12.0
low=balance/12.0
high=(balance*(1+mIR)**12)/12.0
while balance>0:
    checkb=balance
    MinPay=round((low+high)/2,2)
    for x in range(12):
        mUB=checkb-MinPay
        checkb=round(mUB+(mUB*mIR),2)
    if checkb>1:
        low=MinPay
    elif checkb<0:
        high=MinPay
    else:
        break
print('Lowest Payment: '+str(MinPay))