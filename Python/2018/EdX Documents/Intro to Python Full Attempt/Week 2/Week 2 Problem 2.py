# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:58:18 2018

@author: joshc
"""

balance = 4773
annualInterestRate = 0.2
MinPay=0
counter=0
while balance>0:
    checkb=balance
    for x in range(12):
        mIR=annualInterestRate/12.0
        mUB=checkb-MinPay
        checkb=round(mUB+(mUB*mIR),2)
    if checkb>=0:
        MinPay+=10
    else:
        break
print('Lowest Payment: '+str(MinPay))