# coding: utf-8
from random import shuffle
from os import system
data = open('train_data','r').read().split('\n')[:-1]
cmd = (
        "svm-train -s 0 -t 2 -g 0.1 -c 0.1 train model_0",
        "svm-train -s 0 -t 2 -g 1 -c 0.1 train model_1",
        "svm-train -s 0 -t 2 -g 10 -c 0.1 train model_2",
        "svm-train -s 0 -t 2 -g 100 -c 0.1 train model_3",
        "svm-train -s 0 -t 2 -g 1000 -c 0.1 train model_4"
        )
valid = (
        "svm-predict val model_0 tmp > output0",
        "svm-predict val model_1 tmp > output1",
        "svm-predict val model_2 tmp > output2",
        "svm-predict val model_3 tmp > output3",
        "svm-predict val model_4 tmp > output4"
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
ans =  [0,0,0,0,0]
for i in range(100):
    gen_val()
    for train,validation in zip(cmd,valid):
        system(train)
        system(validation)
    result = get_result()
    
    index = -1
    max_val = 0 
    for ind,val in enumerate(result):
        if val > max_val:
            max_val,index = val,ind
    ans[index] +=1
print(ans)
