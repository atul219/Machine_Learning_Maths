import random
import math
import numpy as np
import matplotlib.pyplot as plt

def nck(N,K): # factorial function
    f=math.factorial
    return f(N) // f(K) // f(N-K)

N = 10000
n = 30
CDFProb = 0 
p = 0.7
q = (1-p)

l=[]

# to calculate random values of k or x(Random variable which mean no of times a output occurs).
# we are generating a random probabilty and then we are finding k or x for that particular value(Inverse Transform Sampling).
#cdfprob is cumulative probablity for that particular random varibale.

for i in range(0,N):
    list1 = []
    for j in range(0,n):
        x = 0
        CDFProb = 0
        u = random.uniform(0,1)
        while(CDFProb<=u):
            CDFProb += (nck(n,x)*((p)**x)*((q)**(n-x)))
            x+=1
        list1.append(x)
    l.append(list1)
print(l)

# to calculate mean of N(sample size) values.
# loop to the lenght of list l(there will be 1000 mean of 30 sample size)
meanList = []
for i in l:
    meanList.append(sum(i)/n)
    meanList.sort()
print(meanList)

# sorted mean List to find how many times a mean is occuring.
uniqueList = []
countList = []
number = 0
m = 0
for i in range(0,N):
    if number == meanList[i]:
        countList[m-1] = countList[m-1] + 1
    else:
        number = meanList[i]
        uniqueList.append(number)
        countList.append(int(1))
        m +=1
print(uniqueList)
print(countList)

plt.bar(uniqueList,countList, 0.05)
