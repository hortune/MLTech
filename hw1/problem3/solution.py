from math import sqrt
data =  ((0.533250626258244,2,-2,0,1,0),
(0.0329963769942641,2,0,4,0,4) ,
(0.3669619512516624,2,0,-4,0,4), 
(-0.132638902994687,2,0,2,0,1), 
(-0.8005700515094837,2,0,-2,0,1)) 

result = [0,0,0,0,0]
for i in data:
    result[0] += i[0]*i[1] 
    result[1] += i[0]*i[2] 
    result[2] += i[0]*i[3] 
    result[3] += i[0]*i[4] 
    result[4] += i[0]*i[5] 
    
for i in result:
    print (i)
print (1-(data[0][2]*result[1]+data[0][3]*result[2]+data[0][3]*result[2]+data[0][4]*result[3]+data[0][5]*result[4]))
