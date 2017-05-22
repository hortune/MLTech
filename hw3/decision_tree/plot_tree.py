def load_data(): 
    train_data =[map(float,data.replace('\n','').split()) for data in open('hw3_train.dat').readlines()]
    dim1,dim2,y_train=zip(*train_data)
    x_train = list(zip(dim1,dim2))

    test_data =[map(float,data.replace('\n','').split()) for data in open('hw3_test.dat').readlines()]
    dim1,dim2,y_test=zip(*test_data)
    x_test = list(zip(dim1,dim2))

    return x_train, y_train, x_test, y_test

from sklearn import tree
x_train, y_train, x_test, y_test = load_data()

clf = tree.DecisionTreeClassifier(max_features=2,min_impurity_split = 1e-20)
clf = clf.fit(x_train,y_train)

with open("tree.dot",'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

import pydotplus
dot_data = tree.export_graphviz(clf,out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('tree.pdf')

ypred = clf.predict(x_test)
print("Eout",sum([0 if i==j else 1/len(y_test) for i,j in zip(y_test,ypred)]))
