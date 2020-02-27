#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt

from random_walk import RandomWalk     
rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')    
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()


# In[ ]:


import matplotlib.pyplot as plt

from random_walk import RandomWalk     
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')    
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

