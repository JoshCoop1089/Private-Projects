# -*- coding: utf-8 -*-

import pylab as plt
import random as random
"""
 Visualize how savings changes over time do to differences in interest and deposits
"""

def retire(monthly, rate, terms):
    """
    Inputs:
        Monthly -> Amount to be deposited each month
        rate -> monthly compund interest rate
        term -> length of compunding in months
    
    Outputs:
        base -> list of months
        savings -> amount in account
    """
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate)+monthly]
    return base, savings

def displayRetireWMontlies(monthlies, rate, terms):
    plt.figure("retireMonth")
    plt.clf()
    for monthly in monthlies:
        xVal, yVal = retire(monthly, rate, terms)
        plt.plot(xVal,yVal, label = 'retire:'+str(monthly))
        plt.legend(loc = 'upper left')
        
def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure("retireBoth")
    plt.clf()
    plt.xlim(terms*.75, terms)
    colorList = ['r', 'b', 'k', 'g']
    styleList = ['-', '--', 'o']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        color = colorList[i%len(monthlies)] 
        for j in range(len(rates)):
            rate = rates[j]
            style = styleList[j%len(rates)]
            xVal, yVal = retire(monthly, rate, terms)
            plt.plot(xVal,yVal, color+style, label = 'retire: $'
                     +str(monthly) + " : " + str(int(rate*100)), linewidth = 1.0)
            plt.legend(loc = 'upper left')

possDeposits = [100*i for i in range(5,11,2)]
rate = [i/100 for i in range(3,8,2)]
terms = 40*12
        
displayRetireWMonthsAndRates(possDeposits, rate, terms)