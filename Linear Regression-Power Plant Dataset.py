#!/usr/bin/env python
# coding: utf-8

# In[136]:


import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
powerplant = pd.read_csv('C:/Users/Administrator/Desktop/PYTHON CRASH COURSE/powerplant.csv')
powerplant.head()


# In[132]:


powerplant.info()
powerplant.isnull().values.any()
powerplant.describe()


# In[133]:


pwrplnt =powerplant.drop('PE',axis=1)
pwrplnt.describe()
pwrplnt.info()


# In[ ]:





# In[24]:


pwrplnt.describe()


# In[134]:


pwrplnt.shape


# In[135]:


X= pwrplnt.iloc[:,0]
y1 =pwrplnt.iloc[:,1]
y2=pwrplnt.iloc[:,2]
y3=pwrplnt.iloc[:,3]


# In[50]:


plt.style.use('seaborn')
fig, ax = plt.subplots()

X_20 = X[:20]
y1_20 = y1[:20]


ax.scatter(X_20,y1_20,color='red',s=30)

ax.set_title("Predicting Exhaust Vaccum", fontsize=20,color='green')
ax.set_xlabel("AT(Ambient Temperature)", fontsize=14,color='green')
ax.set_ylabel("V(Exhaust Vaccum)", fontsize=14,color='green')

ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[51]:


plt.style.use('seaborn')
fig, ax = plt.subplots()

X_20 = X[:20]
y2_20 = y2[:20]


ax.scatter(X_20,y2_20,color='green',s=30)

ax.set_title("Predicting Ambient Presssure", fontsize=20,color='green')
ax.set_xlabel("AT(Ambient Temperature)", fontsize=14,color='green')
ax.set_ylabel("AP(Ambient Presssure)", fontsize=14,color='green')

ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()






# In[53]:


plt.style.use('seaborn')
fig, ax = plt.subplots()

X_20 = X[:20]
y3_20 = y3[:20]


ax.scatter(X_20,y3_20,color='blue',s=30)

ax.set_title("Predicting RH(Relative Humidity)", fontsize=20,color='green')
ax.set_xlabel("AT(Ambient Temperature)", fontsize=14,color='green')
ax.set_ylabel("RH(Relative Humidity)", fontsize=14,color='green')

ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()





# In[63]:


X_train = X[:3750]
X_test =X[3750:]

y1_train = y1[:3750]
y1_test = y1[3750:]

y2_train = y2[:3750]
y2_test = y2[3750:]

y3_train = y3[:3750]
y3_test = y3[3750:]

print('Training data size for X is', X_train.shape)
print('Training data size for y1 is', y1_train.shape)
print('Training data size for y2 is',y2_train.shape)
print('Training data size for y3 is', y3_train.shape)

print('Test data size for X is', X_test.shape)
print('Test data size for y1 is' ,  y1_test.shape)
print('Test data size for y2 is' ,  y2_test.shape)
print('Test data size for y3 is' ,  y3_test.shape)





# In[73]:


X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)



# In[78]:


print("The array value for the traing set of X",X_train.shape)


# In[81]:


print("The array value for the traing set of X",X_test.shape)


# In[83]:


regression = linear_model.LinearRegression()
regression.fit(X_train,y1_train)
regression.fit(X_train,y2_train)
regression.fit(X_train,y3_train)


# In[109]:


y_pred = regression.predict(X_test)
print("Prediction for dependent variable",y_pred)


# In[88]:


print("The coefficient for the training dataset is", regression.coef_)


# In[113]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_test, y1_test,color='blue')
ax.plot(X_test,y_pred, color='green',linewidth=3)



   # Set chart title and label axes.
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("AT(Ambient Temperature)", fontsize=14,color='green')
ax.set_ylabel("V(Exhaust Vaccum)", fontsize=14,color='green')

   # Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[130]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.axis([0,40, 0,1150])
ax.scatter(X_test, y2_test,color='blue')

ax.plot(X_test,y_pred, color='green',linewidth=3)



   # Set chart title and label axes.
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("AT(Ambient Temperature)", fontsize=14,color='green')
ax.set_ylabel("AP(Ambient Presssure)", fontsize=14,color='green')

   # Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()


# In[ ]:





# In[107]:


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(X_test, y3_test,color='blue')

ax.plot(X_test,y_pred, color='green',linewidth=3)



   # Set chart title and label axes.
ax.set_title("Linear Regression", fontsize=24,color='green')
ax.set_xlabel("AT(Ambient Temperature)", fontsize=14,color='green')
ax.set_ylabel("RH(Relative Humidity)", fontsize=14,color='green')

   # Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()

