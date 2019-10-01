#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()

import numpy as np
df['timemgmt'] = np.where((df['exercise']<3) & (df['hours']>17), 'busy', 'normal')
df.tail(10)

