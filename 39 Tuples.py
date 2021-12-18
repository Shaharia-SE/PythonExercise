#Create a Tuple

thistuple = ("aplle","banana","orange")
print(thistuple)

# Tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# Tuple Length
# To determine how many items a tuple has, use the len() function

print(len(thistuple))

# Create Tuple With One Item

thistuple = ("apple",) # One item tuple, remember the comma
print(type(thistuple))


thistuple = ("apple")  # #NOT a tuple
print(type(thistuple))



#Tuple Items - Data Types
#String, int and boolean data types

tuple1 = ("apple","banana","orange","kiwi")
tuple2 = (1, 2, 3, 4 , 6 )
tuple3 = (True, False, True)
print(tuple1)
print(tuple2)
print(tuple3)

#A tuple can contain different data types:
#A tuple with strings, integers and boolean values

tuple1 = ("abcd", 34, True, False, "male", "female")
print(tuple1)


#test data type
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

'''
The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
Example
Using the tuple() method to make a tuple:
'''

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
