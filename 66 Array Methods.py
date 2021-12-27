#Array Methods

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Remove all elements from the fruits list
fruits.clear()
print(fruits)

#Copy the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

#Python List count() Method

fruits = ["apple", "banana", "cherry"]
x = fruits.count("apple")
print(x)

#List extend() Method

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#List index() Method
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("apple")
print(x)

#List insert() Method
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#List pop() Method
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)


#List remove() Method
fruits = ['apple', 'banana', 'cherry']
fruits.remove("cherry")
print(fruits)

#List reverse() Method
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#List sort() Method
fruits = ['apple', 'kiwi', 'cherry']
fruits.sort()
print(fruits)
