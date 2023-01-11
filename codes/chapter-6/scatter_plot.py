import matplotlib.pyplot as plt
import numpy as np
mean =0
var = 1
A = 5
simlen = int(1e4)
n= np.random.normal(mean, var, simlen).T
y1 = A+n
y2 = -A+n
plt.plot( y1, 'bx')
plt.plot( y2, 'rx')
plt.legend(['$\mathbf{x} = \mathbf{s}_0$','$\mathbf{x} = \mathbf{s}_1$'])
plt.xlabel("$y_1$")
plt.ylabel("$y_2$")
plt.savefig('scatter.png')
plt.show()
