# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:57:53 2018

@author: joshc
"""
#Homework problem didn't call for a function, but the following recursion does work


#def CCBalance (balance,annualInterestRate,monthlyPaymentRate,months):
#    """
#    Calculates the balance remaining on a credit card after a year
#    Inputs:
#        balance: Starting amount owed
#        annualInterestRate: annual interest rate as a decimal
#        monthlyPaymentRate: percent of total balance paid off per month
#        months: number of months to pay off debt
#    Output:
#        Returns remaining balance after a year
#    """
#    monthlyInterestRate=annualInterestRate/12.0
#    minMonthlyPayment=monthlyPaymentRate*balance
#    monthlyUnpaidBalance=balance-minMonthlyPayment
#    newBalance=round(monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance),2)
#    if months<11:
#        CCBalance(newBalance,annualInterestRate,monthlyPaymentRate,months+1)
#    if months==11:
#        return print('Remaining balance: '+str(newBalance))
#
#
#CCBalance(484,0.2,0.04,0)


balance = 387; annualInterestRate = 0.2; monthlyPaymentRate = 0.06
months=12
#monthlyInterestRate=annualInterestRate/12.0
#minMonthlyPayment=monthlyPaymentRate*balance
#monthlyUnpaidBalance=balance-minMonthlyPayment
#balance=round(monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance),2)
while months>0:
    monthlyInterestRate=annualInterestRate/12.0
    minMonthlyPayment=monthlyPaymentRate*balance
    monthlyUnpaidBalance=balance-minMonthlyPayment
    balance=round(monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance),2)    
    months-=1
print('Remaining balance: '+str(balance))