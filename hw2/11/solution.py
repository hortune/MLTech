# coding: utf-8
import numpy as np
from numpy import genfromtxt
from numpy.linalg import norm, inv
def rbf(gamma, x1,x2):
    return np.exp(-gamma*((x1-x2).dot(x1-x2)))

def Kernel(gamma,data):
    K = np.zeros(data.shape[0]**2).reshape(data.shape[0],data.shape[0])
    for i in range (data.shape[0]):
        for j in range (data.shape[0]):
            K[i][j]=rbf(gamma,data[i],data[j])
    return K

def beta(lamb,gamma,data,y):
    return inv(lamb*np.identity(data.shape[0])+Kernel(gamma,data)).dot(y)


def solve(gamma,b,data,x,y):
    ans = 0
    for test,y_ in zip(x,y):
        summna = 0.
        for bi,train in zip(b,data):
            summna += bi*rbf(gamma,test,train)
        predict = -1 if summna <0 else 1
        ans += 1 if predict != y_ else 0
    return ans

def test(lamb,gamma,x,y,x_val,y_val):
    print "trying lambda",lamb,"gamma",gamma
    b = beta(lamb,gamma,x,y)
    
    print "E_in",solve(gamma,b,x,x,y)/400.
    print "E_out",solve(gamma,b,x,x_val,y)/100.

data = genfromtxt('../data.dat',dtype=np.float32,delimiter=' ')
x,y = data[:,:-1],data[:,-1]
x,x_val,y,y_val = x[:400],x[400:],y[:400],y[400:]
lambset = (0.001,1,1000)
gammaset = (32,2,0.125)
for lamb in lambset:
    for gam in gammaset:
        test(lamb,gam,x,y,x_val,y_val)
