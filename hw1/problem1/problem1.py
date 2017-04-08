import matplotlib.pyplot as plt

x = [(1,0),(0,1),(0,-1),(-1,0),(0,2),(0,-2),(-2,0)]
y = [-1,-1,-1,1,1,1,1]
def gen_z1(x1,x2):
    return 2*x2*x2 - 4*x1 + 1

def gen_z2(x1,x2):
    return x1*x1 - 2*x2 - 3

xpos = [(gen_z1(i[0],i[1]),gen_z2(i[0],i[1])) for (i,j) in zip(x,y) if j == 1 ]
xneg = [(gen_z1(i[0],i[1]),gen_z2(i[0],i[1])) for (i,j) in zip(x,y) if j == -1 ]
print (xpos)

plt.axis([-5,10,-10,5])
plt.plot([z1 for z1,z2 in xpos ],[z2 for z1,z2 in xpos],'o')
plt.plot([z1 for z1,z2 in xneg ],[z2 for z1,z2 in xneg],'x')
plt.show()
