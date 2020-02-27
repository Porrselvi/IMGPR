#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
data = pd.read_csv('C:/Users/Administrator/Desktop/PYTHON CRASH COURSE/WTandHT.csv')
data.head()


# In[10]:


data.info()
data.isnull().values.any()


# In[11]:


data.describe()
data.head()
data.shape


# In[ ]:





# In[12]:


#Training data is
x_data = data.drop('Gender',axis=1)
x_data.shape


# In[13]:


x_data.head()


# In[14]:


x_data[:10]



# In[15]:


X =x_data.iloc[:,0]
y= x_data.iloc[:,1]
#must access through iloc


# In[ ]:





# In[ ]:





# In[16]:


X_20 = X[:20]
y_20 = y[:20]
plt.scatter(X_20,y_20,color='red',s=30)


# In[17]:


#split the data into traning/testing sets
X_train = X[:3000]
X_test =X[3000:]
#split the targets into training/testing sets
y_train = y[:3000]
y_test = y[3000:]


# In[31]:


print('Training data size is', X_train.shape)
print('Training data size is', y_train.shape)
print('Test data size is', X_test.shape)
print('Test data size is' ,  y_test.shape)

#the i/p variable is in the form of vector


# In[39]:


X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)


# In[40]:


print("Training data is in array format for linear regression",X_train.shape)
print("Test data is in in array format for linear regression", X_test.shape)
#array with 1 variable now


# In[44]:


#Linear regression object created
regression = linear_model.LinearRegression()
#using fit function train the traint sets
regression.fit(X_train,y_train)


# In[46]:


#make prediction using the testing set
y_pred = regression.predict(X_test)


# In[70]:


print("Coefficient for training data sets:\n", regression.coef_)


# In[58]:


plt.scatter(X_test, y_test,color='black')
plt.plot(X_test,y_pred, color='green',linewidth=3)

plt.xticks(())
plt.yticks(())
plt.show()


# In[71]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_test, y_test,color='black')
ax.plot(X_test,y_pred, color='green',linewidth=3)



   # Set chart title and label axes.
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("Height", fontsize=14,color='green')
ax.set_ylabel("Weight", fontsize=14,color='green')

   # Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[56]:


print(y_pred)

