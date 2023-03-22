class Student:
    def __init__(self,first_name,last_name,full_name):
        self.first_name=first_name
        self.last_name=last_name
        #self.depar=full_name
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    def email(self):
        return  '{}{}@gmail.com'.format(self.first_name,self.last_name)
obj=Student('shivu','soni','shivu soni') #This is our first object
obj.first_name='manoj' #Here we can change name but if we are not use the property name and full name are differnet
print(obj.full_name)
print(obj.email())

#In the property tag we can use a function as attribute