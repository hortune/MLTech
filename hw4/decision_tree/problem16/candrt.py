from math import sqrt, log
def load_data(): 
    train_data =[map(float,data.replace('\n','').split()) for data in open('../hw3_train.dat').readlines()]
    dim1,dim2,y_train=zip(*train_data)
    x_train = list(zip(dim1,dim2))

    test_data =[map(float,data.replace('\n','').split()) for data in open('../hw3_test.dat').readlines()]
    dim1,dim2,y_test=zip(*test_data)
    x_test = list(zip(dim1,dim2))

    return x_train, y_train, x_test, y_test

def opt_gini(data,dim):
    data = sorted(data, key = lambda tup : tup[dim])
    rf_neg, rf_pos = sum([1 if dat[2]<0 else 0 for dat in data]), sum([1 if dat[2]>0 else 0 for dat in data])
    
    if rf_neg == len(data):
        return -1, -2000, -1, 0
    if rf_pos == len(data):
        return -1, -2000, 1, 0

    min_gin_value = 1 
    lf_neg,lf_pos = 0,0
    optcut = -1

    for i in range(len(data)-1):
        lf_pos += 1 if data[i][2] > 0 else 0
        lf_neg += 1 if data[i][2] < 0 else 0

        rf_pos -= 1 if data[i][2] > 0 else 0
        rf_neg -= 1 if data[i][2] < 0 else 0
        
        gin_left = 1 - (lf_pos/(lf_pos+lf_neg))**2 - (lf_pos/(lf_pos+lf_neg))**2
        gin_right = 1 - (rf_pos/(rf_pos+rf_neg))**2 - (rf_pos/(rf_pos+rf_neg))**2
        gini_impurity = (i+1)*gin_left/(len(data)) + (len(data)-i-1)*gin_right/len(data)

        min_gin_value, optcut = (gini_impurity, i) if gini_impurity <= min_gin_value else (min_gin_value, optcut)
    
    return optcut, (data[optcut][dim] + data[optcut+1][dim])/2, 9487, min_gin_value

def decision_tree(data,dt):
    lt,rt,dim = [],[], 0
    
    split_index,threshold,rp,mg = opt_gini(data,0)
    split_index1,threshold1,rp1,mg1 = opt_gini(data,1) 
    if mg > mg1:
        split_index, threshold, rp, dim = split_index1, threshold1, rp1, 1
    data = sorted(data, key = lambda tup : tup[dim])
    
    #if split_index in (-1, len(data)-1):
    #    dt.append([0,0,0,-1,rp])
    #    return
    #decision_tree(data[:split_index+1],lt)
    #decision_tree(data[split_index+1:],rt)
    counter = 0
    true_count = 0
    for i in range(len(data)):
        if data[i][dim] >= threshold:
            break
        counter += 1
        if data[i][2] > 0:
            true_count += 1
    if true_count >= counter/2:
        rp = 1
    else:
        rp = -1
	
    dt.append([lt,rt,threshold,dim,rp])
    lt.append([0,0,0,-1,rp])
    rt.append([0,0,0,-1,-rp])

def predict(x,model):
    if model[0][3] == -1:
        return model[0][4] # predict answer
    if x[model[0][3]] >= model[0][2]:
        return predict(x,model[0][1])
    return predict(x,model[0][0])

from random import randint
import numpy as np
def bagging(data):
	N = len(data)
	return [data[randint(0,N-1)] for i in range(N)]
	

def random_forest(data,x_train,y_train,x_test,y_test):
	dt_ans  = np.zeros(len(x_test))
	for _ in range(30000):
		my_dt =[]
		decision_tree(bagging(data), my_dt)	
		y_pred = [predict(x,my_dt) for x in x_test]
		dt_ans += np.array(y_pred)
		
		#y_test_pred = [predict(x,my_dt) for x in x_test]
		#Eout = sum([0 if i==j else 1/len(y_test) for i,j in zip(y_test, y_test_pred)])
		#Ein = sum([0 if i==j else 1/len(y_test) for i,j in zip(y_train, y_pred)])
		Eout = sum([0 if i==(1 if j>=0 else -1) else 1/len(y_test) for i,j in zip(y_test,dt_ans)])
		print (Eout)
x_train, y_train, x_test, y_test = load_data()

my_dt =[]

data = [(i[0],i[1],j) for i,j in zip(x_train, y_train)]
random_forest(data,x_train,y_train,x_test,y_test)
#bag = bagging(data)
#decision_tree(data, my_dt)
#decision_tree(bag, my_dt)
"""
y_pred = [predict(x,my_dt) for x in x_train]
y_test_pred = [predict(x,my_dt) for x in x_test]

Eout = sum([0 if i==j else 1/len(y_test) for i,j in zip(y_test, y_test_pred)])
Ein = sum([0 if i==j else 1/len(y_test) for i,j in zip(y_train, y_pred)])
print ("Eout",Eout)
print ("Ein",Ein)
"""
def batch_prediction(x_train,y_train,x_test,y_test,model):
    y_pred = [predict(x,model) for x in x_train]
    y_test_pred = [predict(x,model) for x in x_test]
  
    Eout = sum([0 if i==j else 1/len(y_test) for i,j in zip(y_test, y_test_pred)])
    Ein = sum([0 if i==j else 1/len(y_test) for i,j in zip(y_train, y_pred)])
    print ("Eout",Eout,"Ein",Ein)


def pull_and_travers(x_train,y_train,x_test,y_test,model,my_dt):
    if model[0][3] == -1:
        return
    if model[0][0][0][3] == -1:
        tmp = model[0][0]
        model[0][0] = model[0][1]
        batch_prediction(x_train,y_train,x_test,y_test,my_dt)
        model[0][0] = tmp
    if model[0][1][0][3] == -1:
        tmp = model[0][1]
        model[0][1] = model[0][0]
        batch_prediction(x_train,y_train,x_test,y_test,my_dt)
        model[0][1] = tmp
    pull_and_travers(x_train,y_train,x_test,y_test,model[0][0],my_dt) 
    pull_and_travers(x_train,y_train,x_test,y_test,model[0][1],my_dt)
#pull_and_travers(x_train,y_train,x_test,y_test,my_dt,my_dt)
