#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as pld


# In[3]:


df=pd.read_csv("heart.csv")


# In[4]:


df.head(10)


# In[5]:


new_columns=["Age","Sex","Chest paint","trtbps","chol","fbs","restecg","thalach","exng","oldpeak","slp","caa","thall","output"]


# In[6]:


df.columns=new_columns
df.head(10)


# In[18]:


df.shape
df.info()


# In[19]:


df.isnull()


# In[21]:


df.isnull().sum()


# In[23]:


df.describe()


# In[31]:


df["Chest paint"].value_counts()
df["Chest paint"].value_counts().sum()


# In[27]:


df["Age"].value_counts()


# In[7]:


get_ipython().system(' pip install missingno')


# In[9]:


import missingno


# In[10]:


missingno.bar(df,color='r')


# In[11]:


missingno.dendrogram(df)


# In[12]:


missingno.heatmap(df)


# In[13]:


missingno.matrix(df)


# In[14]:


import seaborn as sns


# In[15]:


sns.distplot(df["Age"],hist_kws=dict(linewidth=1,edgecolor="r"))


# In[16]:





# In[ ]:





# In[ ]:




