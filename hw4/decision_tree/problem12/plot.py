import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

sns.set(color_codes=True)
res = list(map(float,[i for i in open('12_result.txt','r')]))

fig = plt.figure()
sns.distplot(res)
fig.savefig('histogram.png')

