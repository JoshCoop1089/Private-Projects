# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:24:03 2019

@author: joshc

If you feel like it...

A lot of redundant function calls, remake the functions to try and limit cpu use?
"""

#random stat functions
def mean(numberSet, sum = 0):
    for i in range(len(numberSet)):
        sum += numberSet[i]
    avg = sum/len(numberSet)
    return avg

def popVariance(numberSet, mean, sum=0):
    for i in range(len(numberSet)):
        sum += (numberSet[i]-mean)**2.0
    popVar = sum/len(numberSet)
    return popVar

def sampleVariance(numberSet, mean, sum=0):
    for i in range(len(numberSet)):
        sum += (numberSet[i]-mean)**2.0
    sampleVar = sum/(len(numberSet)-1)
    return sampleVar

def meanAbsDeviation(numberSet, mean, sum = 0):
    for i in range(len(numberSet)):
        sum += abs(numberSet[i]-mean)
    return sum/len(numberSet)

def coorelationCoef(xSet, ySet):
    xMean = mean(xSet)
    yMean = mean(ySet)
    xStd = sampleVariance(xSet, xMean) ** 0.5
    yStd = sampleVariance(ySet, yMean) ** 0.5
    # r = 1/n-1(SUM ((xi-xmean)/stdx)*(yi-ymean)/stdy)
    rNval = 1.0/(len(xSet)-1)
    rSum = 0
    for i in range(len(xSet)):
        xRpart = (xSet[i]-xMean)/xStd
        yRpart = (ySet[i]-yMean)/yStd
        rSum += xRpart*yRpart
    r = rNval*rSum
    return r

def statValues(numberSet):
    """Returns mean, popVariance, sampleVariance"""
    numMean = mean(numberSet)
    popVar = popVariance(numberSet, numMean)
    sampleVar = sampleVariance(numberSet, numMean)
    popStdDeviation = popVar**0.5
    sampleStdDeviation = sampleVar**0.5
    mAD = meanAbsDeviation(numberSet, numMean)
    print()
    print(numberSet)
    print("Mean is: ", numMean)
    print("PopVariance is: ", popVar)
    print("SampleVariance is: " , sampleVar)
    print("PopStdDeviation is: ", popStdDeviation)
    print("SampleStdDeviation is: " , sampleStdDeviation)
    print("MeanAbsoluteDeviation is: ", mAD)
    return numMean, popVar, sampleVar

def regressionLine(xSet, ySet):
    """Returns slope, b value, and r value of regression line"""
    xMean, xPopVar, xSampleVar = statValues(xSet)
    yMean, yPopVar, ySampleVar = statValues(ySet)
    r = coorelationCoef(xSet, ySet)
    stdX = xPopVar ** 0.5
    stdY = yPopVar ** 0.5
    slope = r*stdY/stdX
    b = yMean - slope * xMean
    return slope, b, r
      
def regShort(r, xMean, yMean, stdX, stdY):
    slope = r*stdY/stdX
    b = yMean - slope * xMean
    print("\n\nThe regression line is {0:f}x + {1:f}".format(slope, b)) 


regShort(.95,41,33.6,2.3,4.6)

#setLength = int(input("how many numbers are in the set: "))
#numberSet = []
#xyPairs = []
#xSet = []
#ySet = []
#for i in range(setLength):
#    xyPairs.append(tuple(input("Enter x,y: ").split(",")))
#    xSet.append(int(xyPairs[i][0]))
#    ySet.append(int(xyPairs[i][1]))
#slope, b, r = regressionLine(xSet, ySet)
#print("\n\nThe regression line is {0:f}x + {1:f}".format(slope, b))
#print("The R value is: ", r)
#print("with an R^2 value of: ", r ** 2)
 
    
#numberSet.append(float(input("next number is: ")))

