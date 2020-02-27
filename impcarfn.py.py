#!/usr/bin/env python
# coding: utf-8

# In[28]:


import cardetfn
cardetfn.car_detsfnm('Maruthi','2019',color='blue',carn = 'suzuki')
cardetfn.car_detsfnm('Maruthi','2019',color='red',cann='van')


# In[30]:


from cardetfn import car_detsfnm
car_detsfnm('Benz','2019',color='red',cann='car')


# In[31]:


cardetfn.car_detsfnm('Benz','2019',color='red',cann='car')


# In[33]:


from cardetfn import car_detsfnm as adfn
car_detsfnm('Benz','2020',color='Orangered',cann='car')


# In[36]:


import cardetfn as cdtfn
cdtfn.car_detsfnm('Maruthi','2019',color='blue',carn = 'suzuki')


# In[21]:


from cardetfn import *
usinfor('selvi','AP', complang='python',knownlang = 'java')


# In[22]:


def printing_funme(macname,nocps,**docnm):
    docnm['Machine Name'] = macname
    docnm['Number of Copies']= nocps
    return docnm
prdet = printing_funme('Scanner','5',docname='Certificates',type ='Degree')
print(prdet)


# In[8]:





# In[18]:





# In[ ]:


class Car:
      
       
    def __init__(self, make, model, year,odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        #setting a default value for an attribute.
        self.speed = 0
        self.shlspeed =0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def odometer_reading(self):
        print(f"Odometer reading is {self.odometer}")
        
#modyfying an arrtribute value directly
    def speed_limit(self):
        print(f"The speed limit at the school area {self.speed}")
    
    def school_spdlt(self,schoolarealt):
        print(f" The speed limi at the school area {self.shlspeed}")
        if schoolarealt>= self.shlspeed:
            self.shlspeed = schoolarealt
            print("School area limit defined correctly")
        
        else:
            print("It is not defined correctly")     
                      

my_new_car = Car('audi', 'a4', 2019,20)

print(my_new_car.get_descriptive_name())

print(my_new_car.odometer_reading())

sp = my_new_car.speed_limit = 30
print(sp)

splt = my_new_car.school_spdlt = 25
print(splt)

