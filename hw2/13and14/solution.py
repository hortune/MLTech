import os
k =[list(map(float,i.split())) for i in open('../data.dat').readlines()]

fd = open('train','w')
for data in k[:400]:
    input_data = str(int(data[-1]))+" "+" ".join([str(i+1)+':'+str(data[i]) for i in range(len(data)-1)])
    fd.write(input_data+'\n')
fd.close()

fd = open('test','w')
for data in k[400:]:
    input_data = str(int(data[-1]))+" "+" ".join([str(i+1)+':'+str(data[i]) for i in range(len(data)-1)])
    fd.write(input_data+'\n')
fd.close()
os.system('bash train.sh')
parameters =((32,0.001),(2,0.001),(0.125,0.001),(32,1),(2,1),(0.125,1),(32,1000),(2,1000),(0.125,1000))


for  index,par in zip(range(9),parameters):
    print "gamma ",par[0],"C",par[1]
    ans = [1 if float(line)>0 else -1 for line in open('output'+str(index)).readlines()]
    error = 0
    for i in range(100):
        if ans [i] != k[400:][i][-1]:
            error += 1
    print "Eout", error/100.


    ans = [1 if float(line)>0 else -1 for line in open('out'+str(index)).readlines()]
    error = 0
    for i in range(400):
        if ans [i] != k[i][-1]:
            error += 1
    print "Ein", error/400.
