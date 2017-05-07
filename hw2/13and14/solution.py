k =[list(map(float,i.split())) for i in open('../data.dat').readlines()]

fd = open('train','w')
for data in k[:400]:
    input_data = str(int(data[-1]))+" "+" ".join([str(i+1)+':'+str(data[i]) for i in range(len(data)-1)])
    print input_data
    fd.write(input_data+'\n')
fd.close()

fd = open('test','w')
for data in k[400:]:
    input_data = str(int(data[-1]))+" "+" ".join([str(i+1)+':'+str(data[i]) for i in range(len(data)-1)])
    print input_data
    fd.write(input_data+'\n')
fd.close()
