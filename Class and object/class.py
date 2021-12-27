##The __init__() Function
#Create a class named Person, use the __init__() function to assign values for name and age:

##The __init__() Function
#Create a class named Person, use the __init__() function to assign values for name and age:

class Rony:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunction(self):
        print("Hello " , self.name)
        print("my age is " , self.age)

p = Rony("Shharia","24")
p.myfunction()
