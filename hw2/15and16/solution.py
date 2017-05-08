# coding: utf-8
import numpy as np
from numpy import genfromtxt
from numpy.linalg import norm, inv

class LSSVM:
    def __init__(self,data,y,lamb):
        self.data = data
        self.lamb = lamb
        self.y = y
        self.beta()
    def ker(self,x1,x2):
        return x1.dot(x2)

    def Kernel(self):
        K = np.zeros(self.data.shape[0]**2).reshape(self.data.shape[0],self.data.shape[0])
        for i in range (self.data.shape[0]):
            for j in range (self.data.shape[0]):
                K[i][j]=self.ker(self.data[i],self.data[j])
        return K

    def beta(self):
        self.b = inv(self.lamb*np.identity(self.data.shape[0])+self.Kernel()).dot(self.y)

    def activate(self,x):
        """
        INPUT : x array with all train data
        OUPUT : An array y with the ans
        """
        ans = []
        for test in x:
            summna = 0.
            for bi,train in zip(self.b,self.data):
                summna += bi*self.ker(test,train)
            ans.append(-1 if summna <0 else 1)
        return np.array(ans)

data = genfromtxt('../data.dat',dtype=np.float32,delimiter=' ')
np.random.shuffle(data)
train = data[:400]
original_x = data[:400,:-1]
original_y = data[:400,-1]
x_val,y_val = data[400:,:-1],data[400:,-1]
lambset = (0.01,0.1,1,10,100)

for lamb in lambset:
    print "lambda",lamb
    ein_ans = np.zeros(400)
    eout_ans = np.zeros(100)
    for i in range(200):
        np.random.shuffle(train)
        x_train,y_train = train[:200,:-1],train[:200,-1]
        model = LSSVM(x_train,y_train,lamb)
        ein_ans += model.activate(original_x)
        eout_ans += model.activate(x_val)
    ein_ans = [-1 if num<0 else 1 for num in ein_ans]
    eout_ans = [-1 if num<0 else 1 for num in eout_ans]
    
    error = 0
    for i,j in zip(ein_ans,original_y):
        if i != j:
            error += 1
    print "Ein",error/400.

    error = 0
    for i,j in zip(eout_ans,y_val):
        if i != j:
            error += 1
    print "Eout",error/100.
