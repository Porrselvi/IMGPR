#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv
filename = 'C:/Users/Administrator/Desktop/Deep Learning/Breast_cancer_data.csv'
with open(filename) as f:
    reader =csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
for index,column_header in enumerate(header_row):
    print(index,column_header)
    


# In[10]:


import csv
filename = 'C:/Users/Administrator/Desktop/Deep Learning/Breast_cancer_data.csv'
with open(filename) as f:
    reader =csv.reader(f)
    header_row = next(reader)
   # print(header_row)
    
for index,column_header in enumerate(header_row):
    print(index,column_header)
    


# In[19]:


import csv
filename = 'C:/Users/Administrator/Desktop/Deep Learning/Breast_cancer_data.csv'
with open(filename) as f:
    reader =csv.reader(f)
    header_row = next(reader)
    
    peri_high = []

    for row in reader:
        high = float(row[3])
        peri_high.append(high)
    print(peri_high)


# In[1]:


import csv
import matplotlib.pyplot as plt

filename = 'C:/Users/Administrator/Desktop/Deep Learning/Breast_cancer_data.csv'
with open(filename) as f:
    reader =csv.reader(f)
    header_row = next(reader)
    
    peri_high = []

    for row in reader:
        high = float(row[3])
        peri_high.append(high)
    print(peri_high)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(peri_high, c='red')

   # Format plot.
    plt.title("Breast Cancer for Women- 2019", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Mean_Area", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# In[ ]:


class Topic(models.Model):
         
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
                  
        return self.text


# In[5]:


class Entry(models.Model):
    order = models.ForeignKey(MeatOrder, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        
        verbose_name_plural = 'entries'

        def __str__(self):  
            return f"{self.text[:50]}..."


# In[7]:


#"""Defines URL patterns for Online_Meat_Order ."""

from django.urls import path

from . import views

app_name = 'Online_Meat_Order'
urlpatterns = [
# Home page
path('', views.index, name='index'),
   ]


# In[9]:


def index(request):
    #"""The home page for Learning Log."""
    return render(request, 'Online_Order_Meat/index.html')


# In[11]:


<p>
<a href="{% url 'learning_logs:index' %}">Learning Log</a>
</p>

{% block content %}{% endblock content %}



def meatitems(request):
    
    meatitems = MeatOrder.objects.order_by('date_added')
    context = {'meatitems': meatitems}
    return render(request, 'Online_Order_Meat/meatitems.html', context)



# In[14]:


{% extends "Online_Order_Meat/base.html" %}

{% block content %}

    <p>Meat Items</p>

    <ul>
      {% for meatitem in meatitems %}
         <li>{{ meatitems }}</li>
          {% empty %}
         <li>No topics have been added yet.</li>
       {% endfor %}
    </ul>

{% endblock content %}


<p>
    <a href="{% url 'Online_Order_Meat:index' %}">Order Meat By Online</a> 
    <a href="{% url 'Online_Order_Meat:meatitems' %}">Meat Items</a>
</p>


# In[ ]:


def meatitems(request):
        
    topics = MeatOrder.objects.order_by('date_added')
    context = {'meatitems': meatitems}
    return render(request, 'Online_Order_Meat/meatitems.html', context)

