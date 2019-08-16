# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:08:48 2018

@author: joshc
"""

#def fancy_divide(numbers,index):
#    try:
#        denom = numbers[index]
#        for i in range(len(numbers)):
#            numbers[i] /= denom
#    except IndexError:
#        print("-1")
#    else:
#        print("1")
#    finally:
#        print("0")
        
#def fancy_divide(numbers, index):
#    try:
#        denom = numbers[index]
#        for i in range(len(numbers)):
#            numbers[i] /= denom
#    except IndexError:
#        fancy_divide(numbers, len(numbers) - 1)
#    except ZeroDivisionError:
#        print("-2")
#    else:
#        print("1")
#    finally:
#        print("0")


def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
        
fancy_divide([0, 2, 4], 4)