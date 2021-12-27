
#Object Methods

class Rony:
    def __init__(self,name,age):
        self.N = name
        self.A = age

    def myfunction(self):
        print("Hello " + self.N)
        print("my age is " +self.A)

p = Rony("Shaharia","24")
p.myfunction()
