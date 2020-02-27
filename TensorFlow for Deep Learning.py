#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
tf.InteractiveSession()


# In[12]:


a=tf.zeros((4,4))
a.eval()


# In[15]:


b= tf.ones((5,3,4))
b.eval()


# In[23]:


c= tf. fill((2,3), value =9.)
c.eval()


# In[25]:


a= tf.constant(9)
a.eval()


# In[34]:


a= tf.random_normal((2,3), mean=0, stddev=1)
a.eval()


# In[39]:


a= tf.ones((2,2))
b= tf.ones((2,2))
c= a+b
c.eval()

f= 2*c
f.eval()


# In[67]:


c= tf.fill((2,2), value=3)
d = tf.fill((2,2), value =2)
e = c+d
e.eval()


# In[71]:


f=c*d
f.eval()


# In[68]:


i= tf.matmul(c,d)
i.eval()


# In[50]:


g= tf.eye(5)
g.eval()


# In[52]:


h= tf.range(1,6,1)
h.eval()


# In[55]:


r=tf.diag(h)
r.eval()


# In[64]:


c= tf.ones((2,3))
c.eval()



# In[72]:


at=tf.matrix_transpose(c)
at.eval()

#casting functions such as tf.to_double(), tf.to_float(), tf.to_int32(), tf.to_int64(),


# In[77]:


a= tf.ones((2,2))
a.eval()


# In[82]:


b= tf.ones((2,2), dtype=tf.int32)
b.eval()
c=tf.to_float(b)
c.eval()


# In[87]:


sess = tf.Session()
a = tf.ones((2,2))
b= tf.matmul(a,a)
b.eval(session=sess)
sess.run(b)


# In[102]:


a= tf.Variable(tf.ones(2,2))
a


# In[100]:


a.eval()


# In[109]:


sess.run(a.assign(tf.zeros(2,2)))
sess.run(a)

