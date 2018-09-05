# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:28:56 2018

@author: Atul
"""

import matplotlib.pyplot as plt
import numpy as np

def factorial(n):  # factorial function
    if n==0:
        m=1
    else:
        m=n*factorial(n-1)
    return m

def binomial_distribution(n,k,p):  # bionomial probability function
    bd = factorial(n)/((factorial(k))*(factorial(n-k))) *p**k * (1-p)**(n-k)
    return bd

p = 0.5
n = 10
x_axis = np.zeros(11)
y_axis = np.zeros(11)

for i in range(11):
    k = i
    prob = binomial_distribution(n,k,p)
    prob = round(prob,3)
    # plot the graph on x_axis values of k and y_axis prob values
    x_axis[i] = k
    y_axis[i] = prob
    
width = 1/1.5
plt.bar(x_axis,y_axis , width)