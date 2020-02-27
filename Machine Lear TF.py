#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[3]:


print(tf._version_)


# In[4]:


hello=tf.constant("hello")


# In[6]:


type(hello)


# In[23]:


world = tf.constant("World")
type(world)
with tf.Session() as sess:
        result= sess.run(hello+world)


# In[25]:


print(result)


# In[27]:


a=tf.constant(10)
b=tf.constant(20)


# In[29]:


a


# In[31]:


with tf.Session() as sess:
    result = sess.run(a+b)
    


# In[33]:


print(result)


# In[37]:


const=tf.constant(10)
fill_mat=tf.fill((4,4),10)
myzeros = tf.zeros((4,4))
myones = tf.ones((4,4))
myrandn=tf.random_normal((4,4),mean=0,stddev=1.0)
myrandu= tf.random_uniform((4,4),minval=0,maxval=1)
my_ops = [const,fill_mat,myzeros,myones,myrandn,myrandu]
sess= tf.InteractiveSession()
for op in my_ops:
    print(sess.run(op))
    print("\n")


# In[40]:


a= tf.constant([[1,2],[3,4]])
a.get_shape()
b=tf.constant([[10],[20]])
b.get_shape()
result=tf.matmul(a,b)
sess.run(result)


# In[42]:


import tensorflow as tf
n1 = tf.constant(1)
n2=tf.constant(2)
n3 = n1+n2
with tf. Session() as sess:
    result =sess.run(n3)
    print(result)


# In[47]:


sess=tf.InteractiveSession()
my_tensor = tf.random_uniform((4,4),0,1)
my_tensor
my_var = tf.Variable(initial_value=my_tensor)
print(my_var)
init =tf.global_variables_initializer()
sess.run(init)
sess.run(my_var)


# In[50]:


ph = tf.placeholder(tf.float32,shape=(None,4))


# In[75]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import tensorflow as tf
x_data = np.linspace(0.0,10.0,1000000)
noise =np.random.randn(len(x_data))
noise


# In[76]:


noise


# In[70]:





# In[66]:


x_data


# In[132]:


my_data.sample(n=300).plot(kind='scatter',x='X_Data',y='Y')


# In[ ]:


y_true = (0.5*x_data)+5+noise
x_df= pd.DataFrame(data=x_data,columns = ['X Data'])
y_df = pd.DataFrame(data=y_true,columns=['Y'])
my_data=pd.concat([x_df,y_df],axis=1)
my_data.head()
my_data.sample(n=300).plot(kind='scatter',x='X Data',y='Y')


# In[142]:


batch_size =10
m=tf.Variable(2.5)
b=tf.Variable(2.0)
xph = tf.placeholder(tf.float32,[batch_size])
yph= tf.placeholder(tf.float32,[batch_size])
y_model= m*xph+b
error= tf.reduce_sum(tf.square(yph-y_model))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
train =optimizer.minimize(error)
init =tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    batches =1000
    
    for i in range(batches):
        rand_ind =np.random.randint(len(x_data), size=batch_size)
        feed = {xph: x_data[rand_ind],yph:y_true[rand_ind]}
        sess.run(train, feed_dict = feed)
        model_m, model_b = sess.run([m,b])
        y_hat = x_data*model_m + model_b
        my_data.sample(300).plot(kind = 'scatter',x='X Data', y='Y')
    


# In[146]:


Feat_cols =[tf.feature_column.numeric_column('x',shape=[1])]
estimator =tf.estimator.LinearRegressor(feature_columns=Feat_cols)

from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test = train_test_split(x_data,y_true, test_size=0.3,random_state=42)
print(X_train.shape)


# In[189]:


X_test.shape
input_func= tf.estimator.inputs.numpy_input_fn({'x': X_train}, y_train, batch_size =10, num_epochs =None,shuffle=True)
train_input_func= tf.estimator.inputs.numpy_input_fn({'x': X_train}, y_train, batch_size =10, num_epochs =1000,shuffle= False)
test_input_func= tf.estimator.inputs.numpy_input_fn({'x': X_test}, y_test, batch_size =10, num_epochs = 1000,shuffle= False)
estimator.train(input_fn = input_func, steps=1000)

train_metrics =estimator.evaluate(input_fn = train_input_func, steps=1000)
