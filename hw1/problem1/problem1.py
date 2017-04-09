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

fig = plt.figure()
fig.suptitle("|w| in different c",fontsize=20)
plt.xlabel('X',fontsize = 18)
plt.ylabel('Y', fontsize = 16)
plt.axis([-5,10,-10,5])
plt.plot([z1 for z1,z2 in xpos ],[z2 for z1,z2 in xpos],'o')
plt.plot([z1 for z1,z2 in xneg ],[z2 for z1,z2 in xneg],'x')
plt.plot([4,4,4,4,4],[-10,-2,0,2,5],color="red",lw=2)
plt.show()
