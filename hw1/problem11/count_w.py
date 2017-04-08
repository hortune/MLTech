import sys
import matplotlib.pyplot as plt
from math import sqrt
from pylab import *
def w_calculate(name):
    f = open(name,'r').read().split('\n')[8:-1]
    w = [0,0]
    for i in f:
        val = i.split(' ')
        ay = float(val[0])
        x1 = float(val[1].split(':')[1])
        x2 = float(val[2].split(':')[1])
        w[0] += x1*ay
        w[1] += x2*ay
    return sqrt(w[0]**2+w[1]**2)


x = [-5,-3,-1,1,3]
y = []
for i in range(5):
    y.append(w_calculate('model_'+str(i)))

fig = plt.figure()
fig.suptitle("|w| in different c",fontsize=20)
plt.xlabel('C',fontsize = 18)
plt.ylabel('|W|', fontsize = 16)
plt.plot([pow(10,i) for i in x],y,color='blue',lw=2)
plt.xscale('log')
plt.show()
