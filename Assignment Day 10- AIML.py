#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv('general_data.csv')
df.head()


# In[3]:


df.describe()


# # Hypothesis

# ## 1. The average age of the employee leaving the company is equal to 32 years.

# In[6]:


sns.boxplot(x='Attrition', y='Age', data=df)


# ### 2. Maximum number of people leaving the company have distance from home less than or equal to 10.

# In[8]:


plt.figure(figsize=(12,6))
sns.countplot(x='DistanceFromHome', hue='Attrition', data=df)


# ## 3. Maximum number of employee leaving the company are Male

# In[9]:


plt.figure(figsize=(12,6))
sns.countplot(x='Gender', hue='Attrition', data=df)


# ## 4. Maximum number of employee leaving the company are from R&D department

# In[10]:


plt.figure(figsize=(12,6))
sns.countplot(x='Department', hue='Attrition', data=df)


# ## 5. Maximum number of employee leaving the company have average salary of 48000

# In[11]:


plt.figure(figsize=(12,6))
sns.boxplot(x='MonthlyIncome', y='Attrition', data=df)


# ### 6. Number of employee leaving the company have less than or equal 10 total working years

# In[12]:


plt.figure(figsize=(15,6))
sns.boxplot(x='TotalWorkingYears', y='Attrition', data=df)


# ## 7. Number of employee leaving the company have not been promoted since last 2 years

# In[13]:


sns.boxplot(x='YearsSinceLastPromotion', y='Attrition', data=df)


# ## 8. Number of employee who worked in a single company leaves the company most.

# In[14]:


plt.figure(figsize=(15,6))
sns.countplot(x='NumCompaniesWorked', hue='Attrition', data=df)


# ## 9. Employee who have less or rear business travel tends to leave the company.

# In[15]:


plt.figure(figsize=(15,6))
sns.countplot(x='BusinessTravel', hue='Attrition', data=df)


# ## 10. Maximum number of employee leaves the company who have less than 7 years of experience with Current Manager.

# In[16]:


plt.figure(figsize=(15,6))
sns.countplot(x='YearsWithCurrManager', hue='Attrition', data=df)


# ### 11. Maximum number of employee leaving the company have Stock Option Level less than or equal to 1.

# In[17]:


plt.figure(figsize=(15,6))
sns.countplot(x='StockOptionLevel', hue='Attrition', data=df)


# In[ ]:




