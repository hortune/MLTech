from math import sqrt, log
def load_data(): 
    train_data =[map(float,data.replace('\n','').split()) for data in open('hw3_train.dat').readlines()]
    dim1,dim2,y_train=zip(*train_data)
    x_train = list(zip(dim1,dim2))

    test_data =[map(float,data.replace('\n','').split()) for data in open('hw3_test.dat').readlines()]
    dim1,dim2,y_test=zip(*test_data)
    x_test = list(zip(dim1,dim2))

    return x_train, y_train, x_test, y_test

def opt_gini(data,dim):
    total_neg = sum([1 if dat[2]<0 else 0 for dat in data])
    total_pos = sum([1 if dat[2]>0 else 0 for dat in data])
    if total_neg == len(data):
        return -1, -2000, -1
    if total_pos == len(data):
        return -1, -2000, 1
    
    min_gin_value_rp = total_neg
    min_gin_value_rn = total_pos
    gini_rp, optcut1 = total_neg, -1
    gini_rn, optcut2 = total_pos, -1

    for i in range(len(data)):
        gini_rp += 1 if data[i][2] > 0 else -1
        gini_rn += 1 if data[i][2] < 0 else -1
        if (i != len(data)-1 and data[i][dim] != data[i+1][dim]) or i == len(data) -1:
            min_gin_value_rp, optcut1 = (gini_rp, i) if gini_rp < min_gin_value_rp else (min_gin_value_rp, optcut1)
            min_gin_value_rn, optcut2 = (gini_rn, i) if gini_rn < min_gin_value_rn else (min_gin_value_rn, optcut2)
    if min_gin_value_rp < min_gin_value_rn:
        if optcut1 == -1:
            return  -1, -2000, 1
        if optcut1 == len(data)-1:
            return -1,-2000,-1
        return min_gin_value_rp, (data[optcut1][dim] + data[optcut1+1][dim])/2, 1
    else:
        if optcut2 == -1:
            return  -1, -2000, -1
        if optcut2 == len(data)-1:
            return -1,-2000,1
        return min_gin_value_rn, (data[optcut2][dim] + data[optcut2+1][dim])/2, -1


def decision_tree(data,dt,dim):
    data = sorted(data, key = lambda tup : tup[dim])
    lt,rt = [],[]
    split_index,threshold,rp = opt_gini(data,dim)
    if split_index == -1:
        dt.append((0,0,0,-1,rp))
        return
    if split_index == len(data)-1:
        dt.append((0,0,0,-1,-rp))
        return
    decision_tree(data[:split_index+1],lt,not dim)
    decision_tree(data[split_index+1:],rt,not dim)
    
    dt.append((lt,rt,threshold,dim,rp))

def predict(x,model):
    if model[0][3] == -1:
        return model[0][4]
    if x[model[0][3]] >= model[0][2]:
        return predict(x,model[0][1])
    return predict(x,model[0][0])

x_train, y_train, x_test, y_test = load_data()
#x_fake = [(1,0),(0,0),(0,1),(-1,0),(0,-1)]
#y_fake = [1,-1,1,1,1]
my_dt =[]

data = [(i[0],i[1],j) for i,j in zip(x_train, y_train)]
decision_tree(data, my_dt, 0)
y_pred = [predict(x,my_dt) for x in x_train]
y_test_pred = [predict(x,my_dt) for x in x_test]
Eout = sum([0 if i==j else 1/len(y_test) for i,j in zip(y_test, y_test_pred)])
print (Eout)
