#In this module contains, Car and Die classes.
#Car class consists of some following functions - get_descriptive_name(), odometer_reading(),speed_limit(),school_spdl(),user_input(),increment_splimit(), and capacity_fill_gas().




#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Car:
      
       
    def __init__(self, make, model, year,odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        #setting a default value for an attribute.
        self.speed = 0
        self.spdLimit=0
        self.spdLimit1=0
        self.shlspeed =40
        self.incrlt=0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def odometer_reading(self):
        print(f"Odometer reading is {self.odometer}")
        
#modyfying an arrtribute value directly
    def speed_limit(self):
        print(f"The speed limit at the school area {self.speed}")
        
    def school_spdlt(self):
        print(f"The school speed limit is {self.shlspeed}")
        
    def user_input(self):
        spdLimit1 = int(input("Enter the school area speed limit here to know is it correctly defined or not:"))
        print(spdLimit1)
        self.spdLimit= spdLimit1
        print(f"Decleard speed limit is {self.shlspeed}")
        if spdLimit1<= self.shlspeed:
            print(f"The entered {spdLimit1}, and this speed limit is not exceeds the defined speed limit ")
        else:
            print(f"You entered {spdLimit1}, and this speed limit exceeds the oringinal limit ")   
        
    def increment_splimit(self,incrlt):
        self.speed +=incrlt
        
    def capacity_fill_gas(self):
        print("The gas tank cacity is: 40 Gallons")     
        
        
my_new_car = Car('audi', 'a4', 2019,20)

print(my_new_car.get_descriptive_name())

print(my_new_car.odometer_reading())

sp = my_new_car.speed_limit = 30
splt = my_new_car.school_spdlt = 25
my_new_car.user_input()
print(f"Before increment {my_new_car.speed}")
increment = my_new_car.increment_splimit(10)
print(f"After increment {my_new_car.speed}")

my_new_car.capacity_fill_gas()


class Die:
    
    def __init__(self,rl=0,sides=6,sides1=6,sides10=10,sides20=20):
        self.sides = sides
        self.rl= rl
        self.sides1 = sides1 
        self.sides10 = sides10
        self.sides20 = sides20
        
        
    def rol_die(self,sides):
        dies =randint(1,sides)
        print(dies)        
    
            
    def troll(self,rl):            
        rl=1
        while rl<=10:
            dies1 =randint(1,self.sides1)
           # print(dies1)
            print(f"The number {rl} roll and the value in the die is: {dies1}")
            rl+=1
            
    def ten_sided_die(self):
        self.rl=1
        while self.rl<=10:
            times10 = randint(1,self.sides10)
            print(f"The number {self.rl} roll and the value in the die is: {times10}")
            self.rl+=1
            
    def twent_sided_die(self):
        self.rl = 1
        while self.rl <= 10:
            times20 = randint(1,self.sides20)
            print(f"The number {self.rl} roll and the value in the die is: {times20}")
            self.rl += 1
    
                
    
        
die6 = Die()
res = die6.rol_die(6)
res1 = die6.rol_die(6)
die6.rol_die(6)

die6.troll(1)

die6.ten_sided_die()

die6.twent_sided_die()

