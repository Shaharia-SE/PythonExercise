#The self Parameter
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunction(self):
        print("This is ", self.name)
        print("My age is ", self.age)
p1 = person("Shaharia", 24)
p1.myfunction()
