#!/usr/bin/env python
# coding: utf-8

# In[2]:


#plotting simple line graph
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25,36,49,64,81,100]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()


# In[3]:


import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25,36,49,64,81,100]
fig, ax = plt.subplots()
ax.plot(squares,linewidth=5)
ax.set_title("SQUARE NUMBERS",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both',labelsize=14)
plt.show()


# In[4]:


import matplotlib.pyplot as plt
input_val =[1,2,3,4,5,6,7,8,9,10]
squares = [1, 4, 9, 16, 25,36,49,64,81,100]
fig, ax = plt.subplots()
ax.plot(input_val,squares,linewidth=3)
ax.set_title("SQUARE NUMBERS",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both',labelsize=14)
plt.show()

# Here the value started from 1


# In[5]:


import matplotlib.pyplot as plt
input_val =[1,2,3,4,5,6,7,8,9,10]
squares = [1, 4, 9, 16, 25,36,49,64,81,100]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_val,squares,linewidth=3)
ax.set_title("SQUARE NUMBERS",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both',labelsize=14)
plt.show()


# In[6]:


import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2,4, s=200)
ax.set_title("SQUARE NUMBERS",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both',which ='major',labelsize=14)
plt.show()


# In[7]:


import matplotlib.pyplot as plt
input_val =[1,2,3,4,5,6,7,8,9,10]
squares = [1, 4, 9, 16, 25,36,49,64,81,100]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_val,squares,s=150)

ax.set_title("SQUARE NUMBERS",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both',labelsize=14)
plt.show()


# In[8]:


import matplotlib.pyplot as plt
x_val = range(1, 1000)
y_val = [x**2 for x in x_val]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_val,y_val,s=20)

ax.set_title("SQUARE NUMBERS",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both',labelsize=14)
ax.axis([0,1100, 0,1100000])
plt.show()


# In[9]:


import matplotlib.pyplot as plt
x_val = range(1, 1000)
y_val = [x**2 for x in x_val]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_val,y_val,c=y_val, cmap=plt.cm.Blues,s=20)

ax.set_title("SQUARE NUMBERS",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both',labelsize=14)
ax.axis([0,1100, 0,1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')

#trims extra white space -bbox_inches='tight'


# In[14]:


import matplotlib.pyplot as plt
input_val =[1,2,3,4,5,6]
cubes = [1,8,27,64,125,216]
fig, ax = plt.subplots()
ax.plot(input_val,cubes,linewidth=3)
ax.set_title("CUBE NUMBERS",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both',labelsize=14)
plt.show()


# In[25]:


import matplotlib.pyplot as plt
x_val = range(1, 5000)
y_val = [x**3 for x in x_val]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_val,y_val,c=y_val, cmap=plt.cm.Reds,s=20)

ax.set_title("CUBE NUMBERS",fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cube of Values", fontsize=14)
ax.tick_params(axis='both',labelsize=14)
ax.axis([0,1100, 0,1100000])
plt.savefig('cubes_plot.png', bbox_inches='tight')


# In[45]:





# In[8]:





# In[48]:





# In[24]:


import matplotlib.pyplot as plt

from random_walk import RandomWalk     
rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')    
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

