import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = list(map(float,[data for data in open('13_result.txt','r')]))
sns.set(color_codes=True)
sns.set_style("darkgrid")
fig = plt.figure()
plt.plot(data,'o')
fig.savefig('curve.png')
