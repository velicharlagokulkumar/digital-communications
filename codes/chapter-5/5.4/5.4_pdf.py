#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

maxrange=50
maxlim=4.0
x = np.linspace(-2,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('uni1.dat',dtype='double')+np.loadtxt('uni2.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

#def gauss_pdf(x):
#	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)
	vec_tri_pdf = np.piecewise(x, [x < 0, ((x >= 0) & (x < 1)), ((x >= 1) & (x < 2)), x >= 2], [0, lambda x: x, lambda x: 2-x, 0])
#vec_gauss_pdf = scipy.vectorize(gauss_pdf)

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,vec_tri_pdf)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('5.4_pdf.pdf')
plt.show() #opening the plot window
