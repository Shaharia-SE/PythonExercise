#Creating a Function
#In Python a function is defined using the def keyword

def my_function():
    print("Hi Rony This is function")
my_function()

#Arguments
def myfunction(frame):
    print(frame +"Refsnes")
myfunction("Email")
myfunction("windows")
myfunction("Linus")

#Number of Arguments

def myfunction(frame,lname):
    print(frame +" "+lname)
myfunction("Email","Refnse")


def myfunction(*kids):
    print("This is young " + kids[0])
myfunction(" Emai"," facebook"," youtube")


'''
Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
'''

def myfunction(c1, c2, c3):
    print("The youngest child is " +c2)
myfunction(c1 = "Rony", c2 ="jony",c3 = "kony")


#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")



#Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")




#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return Values
def myfunction(x):
    return 5*x
print(myfunction(3))
print(myfunction(6))
print(myfunction(7))


#Recursion Example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

