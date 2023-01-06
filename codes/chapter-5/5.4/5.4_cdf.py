#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

maxrange=50
x = np.linspace(-4,4,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('uni1.dat',dtype='double')+np.loadtxt('uni2.dat',dtype='double')
for i in range(0,maxrange-1):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	vec_tri_cdf = np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x**2/2, lambda x: 2*x - x**2/2 - 1, 1])

plt.plot(x[0:(maxrange-1)].T,err,'o')
#plt.plot(x.T,err)#plotting the CDF
plt.plot(x,vec_tri_cdf)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])
plt.savefig('5.4_cdf.pdf')
plt.show() #opening the plot window
