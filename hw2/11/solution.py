# coding: utf-8
import numpy as np
from numpy import genfromtxt
from numpy.linalg import norm, inv
def rbf(gamma, x1,x2):
    return np.exp(-gamma*norm(x1-x2))

def Kernel(gamma,data):
    K = np.zeros(data.shape[0]**2).reshape(data.shape[0],data.shape[0])
    for i in range (data.shape[0]):
        for j in range (data.shape[0]):
            K[i][j]=rbf(gamma,data[i],data[j])
    return K

def beta(lamb,gamma,data,y):
    return inv(lamb*np.identity(data.shape[0])+Kernel(gamma,data)).dot(y)

def test(lamb,gamma,x,y,x_val,y_val):
    print "trying lambda",lamb,"gamma",gamma
    b = beta(lamb,gamma,x,y)
    w = b.dot(x)
    
    ans = [-1 if data<0 else 1 for data in x.dot(w)]
    error = 0
    for i,j in zip(ans,y):
        if i != j:
            error +=1
    print "E_in",error/400.

    ans = [-1 if data<0 else 1 for data in x_val.dot(w)]
    error = 0
    for i,j in zip(ans,y_val):
        if i != j:
            error +=1
    print "E_out",error/100.

data = genfromtxt('../data.dat',dtype=np.float32,delimiter=' ')
x,y = data[:,:-1],data[:,-1]
x,x_val,y,y_val = x[:400],x[400:],y[:400],y[400:]
lambset = (0.001,1,1000)
gammaset = (32,2,0.125)
for lamb in lambset:
    for gam in gammaset:
        test(lamb,gam,x,y,x_val,y_val)
