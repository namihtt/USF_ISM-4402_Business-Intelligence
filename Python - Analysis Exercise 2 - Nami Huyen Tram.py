#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import library and load data
import pandas as pd
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


#average cars sold per month
df['Cars Sold'].mean()


# In[4]:


#max cars sold per month
df['Cars Sold'].max()


# In[5]:


#min cars sold per month
df['Cars Sold'].min()


# In[6]:


#average cars sold per month by gender
pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[7]:


#average hours worked by people selling > 3 cars per month
df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[8]:


#average years of experience
df['Years Experience'].mean()


# In[9]:


#average years of experience for people selling > 3 cars per month
df[df['Cars Sold']>3]['Years Experience'].mean()


# In[18]:


#average cars sold per month by whether or not they have had sales training
pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[11]:


df.mode().transpose()

data_types = pd.DataFrame(df.dtypes, columns=['Data Type'])
data_types


# In[12]:


missing_data_counts = pd.DataFrame(df.isnull().sum(), columns=['Missing Values'])
missing_data_counts

present_data_counts = pd.DataFrame(df.count(), columns=['Present Values'])
present_data_counts

unique_value_counts = pd.DataFrame(columns=['Unique Values'])
for v in list(df.columns.values):
    unique_value_counts.loc[v] = [df[v].nunique()]
    
unique_value_counts

minimum_values = pd.DataFrame(columns=['Minimum Values'])
for v in list(df.columns.values):
    minimum_values.loc[v] = [df[v].min()]
    
minimum_values

maximum_values = pd.DataFrame(columns=['Maximum Values'])
for v in list(df.columns.values):
    maximum_values.loc[v] = [df[v].max()]
    
maximum_values

# data_quality_report = data_types.join(present_data_counts).join(missing_data_counts).join(unique_value_counts).join(minimum_values).join(maximum_values)

pd.concat([present_data_counts, missing_data_counts, unique_value_counts, minimum_values, maximum_values], axis=1)


# In[13]:


df.corr()


# In[19]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df.hist(column="Hours Worked")


# In[20]:


df.hist(column="Hours Worked", by="Gender")


# In[21]:


df.hist(column="Hours Worked", by="SalesTraining")


# In[ ]:




