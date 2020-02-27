#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class UserDet:
    
    def __init__(self, login_attempts):
        self.login_attempts= login_attempts
        incrattemp=0
        decattempt=0
        
    def user_login(self):
        print(login_attempts)
    
        
    def increment_login_attempts(self,incrattemp):
        self.login_attempts += incrattemp
        print(f"After increment the login attempts are : {self.login_attempts}")
    
    def reset_login_attempts(self,decattempt):
        self.login_attempts-= decattempt
        self.login_attempts=0
        print(f"After decrement the login attempt is : {self.login_attempts}")
        
log = UserDet(10)
log.increment_login_attempts(11)
log.reset_login_attempts(10)

log1 = UserDet(20)
log1.increment_login_attempts(9)
log1.reset_login_attempts(0)



#9.7
class Admin(UserDet):    
    
    def __init__(self,privileges):
        self.privileges = privileges
        login_attempts= 100
        super().__init__(login_attempts)   
       # self.privinher= Privileges()        
        incrattemp=0
        decattempt=0
        
    def show_privileges(self):
        print(f"Can add post")
        print(f"Can delete post {self.privileges}")
        print(f"Can ban post {self.privileges}")
        print(self.privileges)
        
    def user_login(self):
        print(f"Number of login time is {self.login_attempts}")
    
        
    def increment_login_attempts(self,incrattemp):
        self.login_attempts += incrattemp
        print(f"After increment the login attempts are : {self.login_attempts}")
    
        
admindt = Admin('- Adminstraotor')
admindt1 = Admin('I can add post')
admindt2 = Admin('I can delete post')
print(admindt1.privileges)
print(admindt2.privileges)
admindt.show_privileges()
        
admindt.user_login()
admindt.increment_login_attempts(10)

#admindt.privinher.password_change()


#9.8

class Privileges(Admin):
    
    
    def __init__(self,pw):
        self.pw =pw
       # super().__init__(privileges)
              
       # self.reuser = UserDet()
    def password_change(self):
        print(f"Hi {self.pw}")
    
           
        
privs = Privileges('jk')
#privs.show_privileges()
#privs.reuser.user_login()
privs.password_change()

