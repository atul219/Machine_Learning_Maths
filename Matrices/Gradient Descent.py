# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 20:19:30 2018

@author: Atul
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')


lr = 10**-2
esp = 10**-2
i = 0
fx = []
ite = []

# to generate starting value

old_value = np.random.randn(1)
initial_value = old_value
print(old_value)

# coefficient of ploynomial
coef_mat = np.array([8,4,6])
print(coef_mat)

# loop to check function is reaching at minimum point or not
# x = 0
while(True):
        var_mat = np.array([1, old_value[0], old_value[0]**2])
        var_mat = var_mat.reshape(3,1)
        
        operation = coef_mat * var_mat
        

        diff = np.sum(var_mat , axis = 0)
       

        new_value = old_value - lr*diff

        func_initial = 4*initial_value[0] + 2*(initial_value[0]**2) + 3*(initial_value[0]**3)

        func_new = 4*new_value[0] + 2*(new_value[0]**2) + 3*(new_value[0]**3)


        ## print(initial_value , new_value)

        if(abs(initial_value - new_value)<esp)or np.isnan(func_new)==True:
           ## print('hello')
            break;
        initial_value = new_value
        old_value = initial_value

        i+=1
        fx.append(func_initial)
        ite.append(i)
        print(func_initial , func_new)
        
        
   
plt.plot(ite,fx)
