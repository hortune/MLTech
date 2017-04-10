# coding: utf-8
from random import shuffle
import matplotlib.pyplot as plt
from os import system
from math import exp,sqrt
def kernel(x,y):
    delta = (x[0]-y[0])**2+(x[1]-y[1])**2
    return exp(-80*delta)

def manipulate(i):
    data = open('model_'+str(i),'r').read().split('\n')[9:-1]
    data = [qaq.split(' ') for qaq in data]
    data = [(float(num[0]),float(num[1].split(':')[1]),float(num[2].split(':')[1])) for num in data]
    summan = 0
    for i in range(len(data)):
        for j in range(len(data)):
            summan += data[i][0]*data[j][0]*kernel(data[i][1:],data[j][1:])
    return 1/sqrt(summan)

result = [manipulate(i) for i in range(5)]

fig = plt.figure()
fig.suptitle("Distance in different C",fontsize=20)
plt.xlabel('C',fontsize = 18)
plt.ylabel('Distance', fontsize = 16)
x = [-3,-2,-1,0,1]
plt.plot([pow(10,i) for i in x],result,color='blue',lw=2)
plt.xscale('log')
plt.show()
