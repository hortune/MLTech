import sys
from math import sqrt
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
    print ("|w| = ",sqrt(w[0]**2+w[1]**2))

for i in range(5):
    w_calculate('model_'+str(i))
