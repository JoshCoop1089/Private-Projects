# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:42:51 2020

@author: joshc
"""


squared = int(input("What number would you like to find the root of?\t"))
guess = 1
i = 0
while (abs(squared - guess**2) > 0.01):
    y = squared / guess
    guess = (guess + y)/2
    i += 1
print("After {} iterations, the root of {} is {}".format(i, squared, int(guess)))


#BInary search for the int
# low = 1
# high = squared
# i = 0
# while (high > low):
#     i += 1
#     mid = (low + high)//2
#     print(low, mid, high)
#     error = abs(squared - mid**2)
#     if  error < 0.01:
#         guess = int(mid)
#         break
#     elif mid**2 > squared and error > 0.01:
#         high = int(mid - 1)
#     elif mid**2 < squared and error > 0.01:
#         low = int(mid + 1)

x = squared
low = 1
high = x
i = 0
while (high > low):
    i += 1
    mid = (low + high)//2
    error = abs(x - mid**2)
    if  error < 0.01:
        guess =  int(mid)
    elif mid**2 > x and error > 0.01:
        high = mid
    elif mid**2 < x and error > 0.01:
        low = mid
print("After {} iterations, the root of {} is {}".format(i, squared, guess))