#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[12]:


#Create the bin delivers
bins = [0, 80, 100]

#Create names for the four groups
status_names = ['Fail', 'Pass']

df['status'] = pd.cut(df['grade'], bins, labels = status_names)
df


# In[13]:


pd.value_counts(df['status'])


# In[ ]:




