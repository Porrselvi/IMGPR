#!/usr/bin/env python
# coding: utf-8

# In[63]:


import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
powerplant = pd.read_csv('C:/Users/Administrator/Desktop/PYTHON CRASH COURSE/pwrplant.csv')
powerplant.head()


# In[24]:


powerplant.describe()


# In[25]:


powerplant.info()


# In[26]:


powerplant.shape


# In[27]:


X= powerplant.iloc[:,0:4]
y= powerplant.iloc[:,4]


# In[30]:


X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42)


# In[44]:


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[45]:


regression = linear_model.LinearRegression()
regression.fit(X_train,y_train)


# In[47]:


y_pred = regression.predict(X_test)
print(y_pred)


# In[60]:


print('Coefficient for 4 features', regression.coef_)


# In[50]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_train.iloc[:,0],y_train, color='red')

ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("AT(Ambient Temperature)", fontsize=14,color='green')
ax.set_ylabel("Energy output", fontsize=14,color='green')

   # Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[61]:


print('Mean Squared Error:',mean_squared_error(y_test,y_pred))


# In[68]:


print("Variance Score",r2_score(y_test,y_pred))


# In[70]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_train.iloc[:,1],y_train, color='green')
   
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("Ambient Temperature", fontsize=14,color='green')
ax.set_ylabel("Energy output", fontsize=14,color='green')

  
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[67]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_train.iloc[:,1],y_train, color='green')
ax.plot(X_test.iloc[:,1],y_pred,color='red')

   
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("Ambient Temperature", fontsize=14,color='green')
ax.set_ylabel("Energy output", fontsize=14,color='green')

  
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[59]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_train.iloc[:,2],y_train, color='blue')

   
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("Ambient Pressure", fontsize=14,color='green')
ax.set_ylabel("Energy output", fontsize=14,color='green')

  
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[71]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_train.iloc[:,2],y_train, color='blue')
ax.plot(X_test.iloc[:,2],y_pred,color='red')

   
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("Ambient Pressure", fontsize=14,color='green')
ax.set_ylabel("Energy output", fontsize=14,color='green')

  
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[ ]:





# In[56]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_train.iloc[:,3],y_train, color='brown')

   
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("Relative Humidity", fontsize=14,color='green')
ax.set_ylabel("Energy output", fontsize=14,color='green')

  
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[73]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_train.iloc[:,3],y_train, color='brown')
ax.plot(X_test.iloc[:,3],y_pred,color='yellow')

   
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("Relative Humidity", fontsize=14,color='green')
ax.set_ylabel("Energy output", fontsize=14,color='green')

  
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[65]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_train.iloc[:,0],y_train, color='red')
ax.plot(X_test.iloc[:,0],y_pred,color='green')

ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("AT(Ambient Temperature)", fontsize=14,color='green')
ax.set_ylabel("Energy output", fontsize=14,color='green')

   # Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()

