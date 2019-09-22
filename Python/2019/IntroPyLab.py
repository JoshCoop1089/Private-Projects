# -*- coding: utf-8 -*-
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
plt.figure('lin')
plt.clf()
plt.xlabel('sample vals')
plt.ylabel('linear')
plt.title("Linear v Quad")
plt.subplot(311)
plt.ylim(0,800)

#third entry in plt.plot controls color and display style
plt.plot(mySamples, myLinear, 'b+', label = 'linear', linewidth = 3.0)
plt.subplot(313)
plt.ylim(0,800)

plt.plot(mySamples, myQuadratic, 'r--', label = 'quadratic', linewidth = 6.0)
plt.legend(loc = 'upper left')



#plt.figure('cubic')
#plt.plot(mySamples, myCubic)
#plt.figure('expo')
#plt.plot(mySamples, myExponential)
