# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 17:33:54 2017

@author: Josh
"""
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
print("_____________________________")

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
#var='hello, world'
#print(len(var))