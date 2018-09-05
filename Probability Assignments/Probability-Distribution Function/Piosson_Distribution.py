import math
import matplotlib.pyplot as plt
import numpy as np

u = 2
x_axis = np.zeros(11)
y_axis = np.zeros(11)

def factorial(n): # factorial function
    if n == 0:
        m=1
    else:
        m = n*factorial(n-1)
    
    return m

def piosson_distribution(u,k):   # piosson distribution function
    
    pd = (math.exp(-u) * u**k)/factorial(k)
    
    return pd

for i in range(11):
    k = i
    prob = piosson_distribution(u,k)
    prob = round(prob,3)
    x_axis[i] = k
    y_axis[i] = prob
    
plt.plot(x_axis,y_axis)
