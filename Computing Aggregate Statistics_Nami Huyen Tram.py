#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]

GradeList = zip (names, grades, bsdegrees, msdegrees, phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades', 'BS', 'MS', 'PHD'])
df


# In[20]:


df.count()


# In[21]:


df.mean()


# In[22]:


df.std()


# In[23]:


df.min()


# In[24]:


df.max()


# In[25]:


df.quantile(.25)


# In[26]:


df.quantile(.5)


# In[27]:


df.quantile(.75)


# In[ ]:




