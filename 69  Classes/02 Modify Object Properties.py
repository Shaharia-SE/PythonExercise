class persion:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self):
        print("This is ", self.name)
        print("My age ", self.age)


p1 = persion("Shaharia", 24)
p1.name = "Shaharia Safat"
p1.age = 25
p1.myfunction()
