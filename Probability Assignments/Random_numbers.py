
import random
import matplotlib.pyplot as plt


count = 1
random_list = []
unique_list = []
count_un = []

for i in range(0,500):
    random_list.append(random.randint(512,780))
    random_list.sort()
    
number=0 #should not be in the defined range
k=0
for j in range(0,500):
   if number==random_list[j]:
      
       count_un[k-1] = count_un[k-1]+1
       
       #count_un[k]=count_un[k]+1
       
   else:   
       number=random_list[j]
       unique_list.append(random_list[j])
       count_un.append(int(1))
       k=k+1

plt.plot(unique_list,count_un)
plt.ylabel('no. of repetitions')
plt.xlabel('unique no.s')
plt.show()
