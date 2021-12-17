#List append() Method
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)


#Add a list to a list:

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

#List clear() Method
#Remove all elements from the fruits list:

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

#Copy the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)


#Return the number of times the value "cherry" appears in the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)


fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x) #number of 9


#List extend() Method
#Add the elements of cars to the fruits list

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)


#Add a tuple to the fruits list:

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)



# List index() Method
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)



fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)



'''
List insert() Method
Example
Insert the value "orange" as the second element of the fruit list:
'''

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)


#Remove the second element of the fruit list

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)


#Return the removed element

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)


#Remove the "banana" element of the fruit list
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)


#Reverse the order of the fruit list

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)


#Sort the list alphabetically
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)


#Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)


# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)




