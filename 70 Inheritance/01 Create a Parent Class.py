class person:
    def __init__(self, Fname, Lname):
        self.firstname = Fname
        self.lastname = Lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:


x = person("Shaharia", "Rony")
x.printname()
