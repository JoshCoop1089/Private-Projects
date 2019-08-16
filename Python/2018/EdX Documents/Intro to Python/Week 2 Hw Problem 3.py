# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:48:05 2017

@author: Josh
"""

balance=999999
annualInterestRate=0.18
monthInt=annualInterestRate/12
finalbalance=balance
lowBalCheck=round(finalbalance/12,2)
highBalCheck=round((finalbalance*(1+monthInt)**12)/12,2)
monFixed=round(((lowBalCheck+highBalCheck)/2),2)
i=0
while finalbalance>0:
    while i<12:
        BalLeft=finalbalance-monFixed
        finalbalance=round(BalLeft+monthInt*BalLeft,2)
        i+=1
    print('final balance is: ' +str(finalbalance))
    print('monFIxed is: ' +str(monFixed))
    if finalbalance<0 and i==12:
        finalbalance=balance
        highBalCheck=monFixed
        monFixed=round(((lowBalCheck+highBalCheck)/2),2)
        i=0
        print('monFixed was too high, and is now: ' +str(monFixed))
    elif finalbalance>1 and i==12:
        finalbalance=balance
        lowBalCheck=monFixed
        monFixed=round(((lowBalCheck+highBalCheck)/2),2)
        print('monFixed was too low, and is now: ' +str(monFixed))
        i=0  
    elif abs(finalbalance)<1.0:
        break
print('Lowest Payment: ' +str(monFixed))