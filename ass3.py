from random import randint
import random
from numpy import diff
import numpy as np
import matplotlib.pyplot as plt

a=[[0 for i in range(200)] for j in range(200)]      #declaring an array for population
b=[[0 for i in range(200)] for j in range(200)]      #so that the swapped 1 does not change its surroundings in this iteration
iterations=0
for i in range (10):
    a[i][25]=1

while(True):
    for i in range (200):
        for j in range (200):
            if a[i][j]==7:
                if random.random() <= 0.05:  #to check if dead
                    a[i][j]=-404
                else:                       #else gets immuned
                    a[i][j]=-2000
            if a[i][j]>0:
                if random.random() <= 0.05:  #to check if dead
                    a[i][j]=-404                #if suffering add number of days
                else:
                    a[i][j]+=1


# this converts uninfected neighbours infected
    for i in range (200):
        for j in range (200):
            if a[i][j]>0:
                if a[abs(i-1)][j]==0:
                    b[abs(i-1)][j]=1
                if a[(i+1)%200][j]==0:
                    b[(i+1)%200][j]=1
                if a[i][abs(j-1)]==0:
                    b[i][abs(j-1)]=1
                if a[i][(j+1)%200]==0:
                    b[i][(j+1)%200]=1
                if a[abs(i-1)][abs(j-1)]==0:
                    b[abs(i-1)][abs(j-1)]=1
                if a[(i+1)%200][(j+1)%200]==0:
                    b[(i+1)%200][(j+1)%200]=1
                if a[(i+1)%200][abs(j-1)]==0:
                    b[(i+1)%200][abs(j-1)]=1
                if a[abs(i-1)][(j+1)%200]==0:
                    b[abs(i-1)][(j+1)%200]=1

#this is to save swap changes in main array
    for i in range (200):
        for j in range (200):
            if b[i][j]==1 and a[i][j]==0:
                a[i][j]=1
# this just to swap 10 independent indices to different 10 indices
    list1=[]
    while(len(list1)!=10):
      a1= randint(0,199)
      b1= randint(0,199)
      if [a1,b1] not in list1:
        list1.append([a1,b1])
    list2=[]
    while(len(list2)!=10):
      c1=randint(0,199)
      d1=randint(0,199)
      if [c1,d1] not in list1 and [c1,d1] not in list2:
        list2.append([c1,d1])

    for x in range (10):
      temp=a[(list1[x][0])][(list1[x][1])]
      a[(list1[x][0])][(list1[x][1])]=a[(list2[x][0])][(list2[x][1])]
      a[(list2[x][0])][(list2[x][1])]=temp
#this is to count people from each category
    iterations+=1
    count=0
    illcount=0
    deadcount=0
    immcount=0
    for i in a:
        for j in i:
            if(j>0):
                illcount+=1
            if(j== -404):
                deadcount+=1
            if(j== -2000):
                immcount+=1
    count=illcount+deadcount+immcount
    if (count==40000):
        break

print(iterations)
print(deadcount/400)
print(immcount/400)
print(illcount/400)
