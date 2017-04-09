# coding: utf-8
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
        "svm-predict train_data model_0 tmp > output0",
        "svm-predict train_data model_1 tmp > output1",
        "svm-predict train_data model_2 tmp > output2",
        "svm-predict train_data model_3 tmp > output3",
        "svm-predict train_data model_4 tmp > output4"
        )

def gen_val():
    shuffle(data)
    with open('val','w') as fd:
        for i in data[:1000]:
            print(i, file=fd)
    with open('train','w') as fd:
        for  i in data[1000:]:
            print(i,file=fd)

def get_result():
    result = [float(open('output'+str(i),'r').read().split(' ')[2][:-1]) for i in range(5)]
    return result


for validation in valid:
    system(validation)
result = get_result()
print (result)
fig = plt.figure()
fig.suptitle("Ein in different C",fontsize=20)
plt.xlabel('C',fontsize = 18)
plt.ylabel('Ein', fontsize = 16)
x = [-5,-3,-1,1,3]
plt.plot([pow(10,i) for i in x],result,color='blue',lw=2)
plt.xscale('log')
plt.show()
