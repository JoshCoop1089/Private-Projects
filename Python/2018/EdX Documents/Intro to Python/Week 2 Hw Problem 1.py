# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:27:55 2017

@author: Josh
"""

#def debt(balance, annualInterestRate, monthlyPaymentRate,months):
#    '''
#    Input: 
#        balance-> outstanding balance on card
#        annualInterestRate -> rate as a decimal
#        monthlyPaymentRate -> minimum payment as decimal
#    Output:
#        unpaid -> balance left for next month
#    '''
#    monthInt=annualInterestRate/12
#    minMonthPayment=monthlyPaymentRate*balance
#    BalLeft=balance-minMonthPayment
#    NewBal=round(BalLeft+monthInt*BalLeft,2)
#    if months>1:
#        print ('Month Balance is: ' + str(NewBal))
#        return debt(NewBal,annualInterestRate, monthlyPaymentRate, months-1)
#    else:
#        return print('Remaining balance: '+str(NewBal))
 

balance=42
annualInterestRate=0.2
monthlyPaymentRate=0.04 
monthInt=annualInterestRate/12
i=0
while i<12:
    minMonthPayment=monthlyPaymentRate*balance
    BalLeft=balance-minMonthPayment
    balance=round(BalLeft+monthInt*BalLeft,2)
    i+=1
    print ('Remaining balance: '+str(balance))    