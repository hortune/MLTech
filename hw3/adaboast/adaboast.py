from math import sqrt, log
def load_data(): 
    train_data =[map(float,data.replace('\n','').split()) for data in open('hw3_train.dat').readlines()]
    dim1,dim2,y_train=zip(*train_data)
    x_train = list(zip(dim1,dim2))

    test_data =[map(float,data.replace('\n','').split()) for data in open('hw3_test.dat').readlines()]
    dim1,dim2,y_test=zip(*test_data)
    x_test = list(zip(dim1,dim2))

    return x_train, y_train, x_test, y_test

def find_decision_stump(data,dim):
    data = sorted(data, key = lambda tup : tup[dim])
    total_neg =sum([i[3] for i in data if i[2] < 0 ])
    total_pos =sum([i[3] for i in data if i[2] >= 0])

    curr_pen_rp, cut1 = total_neg, -1
    curr_pen_rn, cut2 = total_pos, -1
    
    min1, opt_cut1 = curr_pen_rp, -1
    min2, opt_cut2 = curr_pen_rn, -1
    
    for i in range(len(data)):
        curr_pen_rp += data[i][3] if data[i][2] > 0 else -data[i][3]
        
        if (i!= len(data) - 1 and data[i][dim] != data[i+1][dim]) or i == len(data):
            (min1,opt_cut1) = (curr_pen_rp,i) if curr_pen_rp < min1 else (min1,opt_cut1)
        
        curr_pen_rn += data[i][3] if data[i][2] < 0 else -data[i][3]
        
        if (i!= len(data) - 1 and data[i][dim] != data[i+1][dim]) or i == len(data):
            (min2,opt_cut2) = (curr_pen_rn,i) if curr_pen_rn < min2 else (min2,opt_cut2)
    
    if min1 <= min2:
        index = opt_cut1
        epsilon = min1/(total_neg + total_pos)
        threshold = (data[opt_cut1][dim]+data[opt_cut1+1][dim])/2 if opt_cut1 != (len(data)-1) else 99999999 
        
        change_var = sqrt((1-epsilon)/epsilon)

        new_weighted_data = []
        for subdata in data[:index+1]:
            if subdata[2] == -1:
                new_weighted_data.append((subdata[0],subdata[1],subdata[2],subdata[3]/change_var))
            else:
                new_weighted_data.append((subdata[0],subdata[1],subdata[2],subdata[3]*change_var))
        for subdata in data[index+1:]:
            if subdata[2] == 1:
                new_weighted_data.append((subdata[0],subdata[1],subdata[2],subdata[3]/change_var))
            else:
                new_weighted_data.append((subdata[0],subdata[1],subdata[2],subdata[3]*change_var))
        return new_weighted_data, threshold, log(change_var), 1, min1/len(data), epsilon
    
    else:
        index = opt_cut2
        epsilon = min2/(total_neg + total_pos)
        threshold = (data[opt_cut2][dim]+data[opt_cut2+1][dim])/2
        change_var = sqrt((1-epsilon)/epsilon)

        new_weighted_data = []
        for subdata in data[:index+1]:
            if subdata[2] == 1:
                new_weighted_data.append((subdata[0],subdata[1],subdata[2],subdata[3]/change_var))
            else:
                new_weighted_data.append((subdata[0],subdata[1],subdata[2],subdata[3]*change_var))
        for subdata in data[index+1:]:
            if subdata[2] == -1:
                new_weighted_data.append((subdata[0],subdata[1],subdata[2],subdata[3]/change_var))
            else:
                new_weighted_data.append((subdata[0],subdata[1],subdata[2],subdata[3]*change_var))
        return new_weighted_data, threshold, log(change_var), -1, min2/len(data), epsilon

def make_decision_stump(data):
    
    nwd0, thres0, weight0, rp0, einu0, eps0 = find_decision_stump(data,0)
    nwd1, thres1, weight1, rp1, einu1, eps1 = find_decision_stump(data,1)
   
    if einu0<einu1:
        return nwd0, thres0, weight0, rp0, 0, eps0
    else:
        return nwd1, thres1, weight1, rp1, 1, eps1

def adaboast(x,y):
    hypothesis = []
    u = [1/len(x) for i in range(len(x)) ]
    data = [(nx[0],nx[1],ny,nu) for nx,ny,nu in zip(x,y,u)]
    
    for i in range(300):
        usum = sum([dat[3] for dat in data])
        data, thres, weight, rp, dim, eps = make_decision_stump(data)
        hypothesis.append((thres,weight,rp,dim,eps,usum))
    return hypothesis

def activation(x,hypothesis):
    y_pred = []
    for i in range(len(x)):
        ans = 0
        for hyp in hypothesis:
            if x[i][hyp[3]] >= hyp[0]:
                ans += hyp[1]*hyp[2]
            else:
                ans -= hyp[1]*hyp[2] 
        if ans >= 0:
            y_pred.append(1)
        else:
            y_pred.append(-1)
    return y_pred
"""
some mistake here and i don't know why
def Ein(x,y,hypo):
    ein = 0
    for i,j in zip(x,y):
        if i[hypo[3]] >= hypo[0] and j != hypo[2]:
            ein += 1
        else:
            if j == hypo[2]:
                ein += 1
    return ein/len(x)
"""
x_train, y_train, x_test, y_test = load_data()
hypothesis =  adaboast(x_train, y_train)
y_pred = activation(x_test,hypothesis)

def Ein_count(y_train,y_pred):
    ein = 0
    for i,j in zip(y_pred,y_train):
        if i != j:
            ein+=1
    return ein/len(y_train)

import matplotlib.pyplot as plt
import numpy as np

#Problem 7 & 8
fig = plt.figure()
print ("hypo1 alpha",hypothesis[0][1])
Ein_per = [Ein_count(activation(x_train,[hypo]),y_train) for hypo in hypothesis]
print ("Ein_per hypo[0]", Ein_per[0])
plt.plot(np.arange(300),Ein_per)
fig.savefig('Ein_per')
fig.clf()

# Problem 9
Ein_cum = [Ein_count(activation(x_train,hypothesis[:i+1]),y_train) for i in range(len(hypothesis))]
print ("Ein_cum[G]",Ein_cum[-1])

plt.plot(np.arange(300),Ein_cum)
fig.savefig('Ein_cum')
fig.clf()

# Problem 10
ut= [hypo[5] for hypo in hypothesis]
#print ("U_t", ut)
print('ut[1]',ut[1],'ut[-1]',ut[-1])
plt.plot(np.arange(300),ut)
fig.savefig('U_t')
fig.clf()

# Problem 11
epsion_set = [hypo[4] for hypo in hypothesis]
print ("min(epsilon)",min(epsion_set))
plt.plot(np.arange(300),epsion_set)
fig.savefig('Epsilon')
fig.clf()

# Problem 12
Eout_per = [Ein_count(activation(x_test,[hypo]),y_test) for hypo in hypothesis]
print ("Eout_per g1", Eout_per[0])
plt.plot(np.arange(300),Eout_per)
fig.savefig('Eout_per')
fig.clf()


# Problem 13
Eout_cum = [Ein_count(activation(x_test,hypothesis[:i+1]),y_test) for i in range(len(hypothesis))]
print ("Eout_cum G", Eout_cum[-1])
plt.plot(np.arange(300),Eout_cum)
fig.savefig('Eout_cum')
fig.clf()
