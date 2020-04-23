#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as nr
import math
from sklearn import preprocessing
import sklearn.model_selection as ms
from sklearn import linear_model
import sklearn.metrics as sklm

get_ipython().run_line_magic('matplotlib', 'inline')


# In[67]:


database_a=database_b= pd.read_csv(r"C:\Users\kamra\Downloads\Songs_LA.csv")
database_a.drop("Unnamed: 1", axis=1, inplace=True)
database_a.columns


# In[68]:


database_a.head()


# In[69]:


df = database_a.drop("songs", axis=1)
database_a.head()


# In[70]:


df["Mood"] = df.idxmax(axis=1)


# In[71]:


database_a["Mood"] = database_b["Mood"] = df["Mood"]


# In[72]:


database_b.head()


# In[55]:


print( 'Select your song from this list:  ') 
print ( database_a['songs'])


# In[73]:


song1 = input("Enter song name : " )
print ('Currently playing: ' +song1)


# In[74]:


for songnum in range (60):
    if song1 == database_a['songs'][songnum]:
        break
        
print (songnum)


# In[79]:


def nearestneighbour(df, songnum):
    min=100
    for i in range (60):
        if df['Mood'][i]== df['Mood'][songnum] and i!=songnum:
            distancesq = (df['happy'][i]- df['happy'][songnum])**2 + (df['sad'][i]- df['sad'][songnum])**2 + (df['fast'][i]- df['fast'][songnum])**2 + (df['romance'][i]- df['romance'][songnum])**2
            dist= math.sqrt(distancesq)
            if dist< min:
                min= dist
                nextsong=df['songs'][i]
    return nextsong

print ('Next song :'  + nearestneighbour(database_a, songnum))
        
        


# In[ ]:




