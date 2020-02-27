#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()


# In[8]:


print("Image Dta Shape", digits.data.shape)
print("Label Dta Shape", digits.target.shape)


# In[10]:


plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(digits.data[0:5],digits.target[0:5])):
    plt.subplot(1,5,index+1)
    plt.imshow(np.reshape(image,(8,8)), cmap=plt.cm.gray)
    plt.title('Training: %i\n' % label,fontsize=20)


# In[12]:


from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test = train_test_split(digits.data, digits.target, test_size=0.25,random_state=0)


# In[13]:


from sklearn.linear_model import LogisticRegression


# In[16]:


logisregg = LogisticRegression()
logisregg.fit(X_train,y_train)


# In[20]:


predictions = logisregg.predict(X_test)
print(predictions)


# In[21]:


scoreval = logisregg.score(X_test,y_test)
print(scoreval)

