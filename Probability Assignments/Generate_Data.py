
import random 
import math
import matplotlib.pyplot as plt
import numpy as np


Mean = 10.6
StdDev = 3.5

Observations = []
X_axis = np.linspace(-3.4,24.6,20)
BarWidth = (24.6 + 3.4)/20
Frequency = [0] * X_axis

for i in range(0,1000):
    
    StdDevMultiply = random.uniform(1,4)
    
    Observations.append(Mean + (StdDevMultiply*StdDev))
    
    Observations.append(Mean - (StdDevMultiply*StdDev))
    
    Observations.sort()
    
print(Observations)

for Ob in Observations:
    
    Frequency[math.floor((Ob -(-3.4))/BarWidth)] += 1
    
print(Frequency)

plt.bar(X_axis,Frequency,5.6)
