#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[12]:


def gen_to_num(x):
    if x == 'female':
        return 1
    if x == 'male':
        return 0


# In[13]:


df['gender_val'] = df['gender'].apply(gen_to_num)
df.tail()


# In[14]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours + gender_val', data=df).fit()
result.summary()


# In[16]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours + gender_val', data=df).fit()
result.summary()


# In[21]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours', data=df).fit()
result.summary()


#I can add gender to my regression. It does improve my R-squared, but not significant, from 66.4% to 66.5% 
#If it does, it means that the strength of the relationship between my model and the dependent variable is 66.5%.


# In[ ]:




