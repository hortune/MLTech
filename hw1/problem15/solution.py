#coding: utf-8
from random import shuffle
import matplotlib.pyplot as plt
from os import system
cmd = (
        "svm-train -s 0 -t 2 -g 0.1 -c 0.1 train model_0",
        "svm-train -s 0 -t 2 -g 1 -c 0.1 train model_1",
        "svm-train -s 0 -t 2 -g 10 -c 0.1 train model_2",
        "svm-train -s 0 -t 2 -g 100 -c 0.1 train model_3",
        "svm-train -s 0 -t 2 -g 1000 -c 0.1 train model_4"
        )
valid = (
        "svm-predict test_data model_0 tmp > output0",
        "svm-predict test_data model_1 tmp > output1",
        "svm-predict test_data model_2 tmp > output2",
        "svm-predict test_data model_3 tmp > output3",
        "svm-predict test_data model_4 tmp > output4"
        )

def get_result():
    result = [float(open('output'+str(i),'r').read().split(' ')[2][:-1]) for i in range(5)]
    return result

for i in range(5):
    system(valid[i])

result = get_result()
print (result)
fig = plt.figure()
fig.suptitle("Eout in different gamma",fontsize=20)
plt.xlabel('C',fontsize = 18)
plt.ylabel('Eout', fontsize = 16)
x = [0,1,2,3,4]
plt.plot([pow(10,i) for i in x],[100-i for i in result],color='blue',lw=2)
plt.xscale('log')
plt.show()
