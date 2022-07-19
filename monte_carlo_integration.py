from scipy import random
import numpy as np


#limits of integration
a = 0
b = np.pi

#number of tries
N = 5000

#iterating over each value of arr and filling it with a random
#value between the limits a and b

arr = np.random uniform(a,b,N)

#a value is passed into the parameter and the function returns the computed 
#vale

def f_sine():
	return np.sin(x)

#iterates and sums up values of different results of the function above using
# a generator expression	
  	
integral = sum(f_sine(x) for x in arr)

answer = (b-a)/float(N)

print("The result is:", answer)