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
    
    print("curr_pen_rp",curr_pen_rp)
    print("curr_pen_rn",curr_pen_rn)
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
        print ("epsilon", epsilon)
        
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
        print("=================================")
        return new_weighted_data, threshold, log(change_var), 1, min1/len(data) 
    
    else:
        index = opt_cut2
        epsilon = min2/(total_neg + total_pos)
        print ("epsilon", epsilon)
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
        print("=================================")
        return new_weighted_data, threshold, log(change_var), -1, min2/len(data)

def make_decision_stump(data):
    
    nwd0, thres0, weight0, rp0, einu0 = find_decision_stump(data,0)
    nwd1, thres1, weight1, rp1, einu1 = find_decision_stump(data,1)
   
    if einu0<einu1:
        return nwd0, thres0, weight0, rp0, 0
    else:
        return nwd1, thres1, weight1, rp1, 1

def adaboast(x,y):
    hypothesis = []
    u = [1/len(x) for i in range(len(x)) ]
    data = [(nx[0],nx[1],ny,nu) for nx,ny,nu in zip(x,y,u)]
    
    for i in range(300):
        data, thres, weight, rp, dim = make_decision_stump(data)
        hypothesis.append((thres,weight,rp,dim))
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


x_train, y_train, x_test, y_test = load_data()
x_fake = [(0,0),(1,0),(0,1),(-1,0),(0,-1)]
y_fake = [1,-1,-1,-1,-1]
hypothesis =  adaboast(x_train, y_train)
y_pred = activation(x_test,hypothesis)
