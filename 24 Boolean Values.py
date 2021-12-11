print(100 > 99)
print(100 == 90)
print(100 < 90)

#Print a message based on whether the condition
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#The following will return True:
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#The following will return False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


#a __len__ function that returns 0 or False
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))