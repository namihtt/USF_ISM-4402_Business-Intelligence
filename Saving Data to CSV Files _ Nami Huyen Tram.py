#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegress = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = zip(names,grades,bsdegress,msdegrees,phddegrees)
columns=['Names','Grades','BS','MS','PhD']
df = pd.DataFrame(data = Degrees, columns = columns)
df.to_csv('savecsvchallenge.csv', index=False, header=True)


# In[ ]:




