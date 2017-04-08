# coding: utf-8
f = open('features.test','r')
data = f.read().split('\n')
data =[list(map(float,i.split())) for i in data]
for i in data:
    if len(i) == 0:
        continue
    if i[0] == 8.0:
        print ("+1","1:"+str(i[1]),"2:"+str(i[2]))
    else:
        print ("-1","1:"+str(i[1]),"2:"+str(i[2]))
