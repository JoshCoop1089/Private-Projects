# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:53:18 2017

@author: Josh
"""

balance=320000
annualInterestRate=0.2
monthInt=annualInterestRate/12
finalbalance=balance
monFixed=0
i=0
while finalbalance>0:
    while i<12:
        BalLeft=finalbalance-monFixed
        finalbalance=round(BalLeft+monthInt*BalLeft,2)
        i+=1
    if finalbalance>0 and i==12:
        finalbalance=balance
        monFixed+=10
        i=0
    else:
        break
print('Lowest Payment: ' +str(monFixed))