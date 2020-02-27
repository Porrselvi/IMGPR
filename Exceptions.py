#!/usr/bin/env python
# coding: utf-8

# In[6]:


with open('PythText.txt') as file_object:
    contents = file_object.read()
    print(contents)


# In[9]:


with open('PythText.txt') as read_pyfile:
    contfile = read_pyfile.read()
    print(contfile.rstrip())
    
# here I omit the extraw space bu using rstrip() method


# In[29]:


file_path = 'Downloads\PythText.txt'
with open(file_path) as file_read:
    filecont = file_read.read()
    num_string = ' '
for finfo in filecont:
    num_string += finfo.rstrip()
print(num_string)
print(f"{num_string[:52]} ...")
print(len(num_string))
    
    


# In[5]:


file_path = 'Downloads\PythText.txt'
with open(file_path) as file_read:
    filecont = file_read.read()
    num_string = ' '
for finfo in filecont:
    num_string += finfo.rstrip()
birthday = input("Enter your birthday")
if birthday in num_string:
    print(f"Your birthday appear in pi-string {birthday}")
else:
    print("Your birthday is not appear")


# In[13]:


file_name = ('Downloads\PythonLearn.txt')
with open(file_name) as learn_python:
    fcont = learn_python.read()
    print(f"After reading the entire file {fcont}")
    i=1
    while i<=3:
        i=i+1
        print(fcont)
    nu_string =''
for content in fcont:
    nu_string+= content.rstrip()
print(f"Reading through for loop: {nu_string}")

file_list = [fcont]
print(f"Printing from the list {file_list}")


# In[12]:


i=0
while i<4:
    i=i+1
    print(i)
    


# In[15]:


file_name = ('Downloads\PythonLearn.txt')
with open(file_name) as learn_python:
    fcont = learn_python.read()
    print(f"After reading the entire file {fcont}")
    recont = fcont.replace('python','C')
    print(recont)


# In[2]:


file_name = 'Downloads\PythonWrite.txt'

with open(file_name,'w') as write_object:
    write_object.write("I am learning Python program efficiently \n")
    write_object.write("Python programming is very interesting \n")
    


# In[6]:


file_name = 'Downloads\PythonWrite.txt'

with open(file_name) as read_object:
    readfile= read_object.read()
    print(readfile)


# In[7]:


file_name = 'Downloads\PythonWrite.txt'

with open(file_name,'a') as write_object:
    write_object.write("I am learning 'Java' program efficiently \n")
    write_object.write("Java programming is very interesting to study\n")
    


# In[ ]:


fil_nm ='Userinput.txt'

with open(fil_nm,'w') as write_newfile:
    active=True
    
    while active:
        user_input = input("Enter your first name and this name will store in a file: ")
        user_input1 = input("Enter your last name and this name will store in a file: ")
    
        write_newfile.write(f"{user_input}\n")
        write_newfile.write(user_input1)         
        if user_input1 =='quit':
            active=False
        else:
            print("")
    
    
        


# In[5]:


file_name = 'Userinput.txt'

with open(file_name) as read_object:
    readfile= read_object.read()
    print(readfile)


# In[59]:


guest = 'GuestBook.txt'
with open(guest,'w') as guest_file:
    user_input = input("Enter your name")
    mess= (f"Hi {user_input} your name has added in the file, congrates")
    print(f"{mess}")
    guest_file.write(f"{user_input}\n")
    guest_file.write(mess)


# In[4]:


fil_nm ='Userinput1.txt'

with open(fil_nm,'w') as write_newfile:  
               
    active=True         
    while active:
        user_input = input("Enter your first name and this name will store in a file: ")
           # user_input1 = input("Enter your last name and this name will store in a file: ")
        write_newfile.write(user_input)         
            
            
        if user_input == 'quit':
            active=False
        else:
            print(user_input)
   
    
#write_newfile.write(f"{user_input}\n")

    
    


# In[4]:


fil_nm ='Userinput1.txt'
 
active1 = True
while active1:  
    with open(fil_nm,'w') as write_newfile:
                       
        active=True         
        while active:
            user_input = input("Enter your first name and this name will store in a file: \n ")
           # user_input1 = input("Enter your last name and this name will store in a file: ")
            write_newfile.write(f"{user_input}\n")             
            if user_input == 'quit':
                active=False
            else:
                print(user_input)
    user_input1 = input("Close a file: ")
    if user_input1=='Close':
        active1= False
    else:
        print('')
    
     
    


# In[8]:




print(0/5)

try:
    print(5/0)
except ZeroDivisionError:
    print("I can't calculate number / 0")


# In[ ]:





# In[ ]:




