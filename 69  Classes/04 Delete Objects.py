# Delete Objects
# You can delete objects by using the del keyword:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

del p1
p1.myfunc()
print(p1)
