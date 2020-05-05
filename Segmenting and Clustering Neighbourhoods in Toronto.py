#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
get_ipython().system('pip install xlrd')


# In[31]:


toronto_data = pd.read_excel (r'toronto.xlsx') #read into the dataset
toronto_data = toronto_data[toronto_data.Borough != 'Not assigned'] #drop columns with Borough "Not assigned"
toronto_data["Neighborhood"] = toronto_data["Neighborhood"].str.replace("/", ",") #replace / with ,
toronto_data.head()


# In[32]:


toronto_data.shape

