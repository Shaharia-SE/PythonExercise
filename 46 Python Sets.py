# create a set
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.

thisset = {"apple", "banana", "cherry"}
print(thisset)



#Duplicates Not Allowed
#Sets cannot have two items with the same value.
thisset = {"apple","banana","cherey","orange","apple"}
print(thisset)



#Get the Length of a Set
#To determine how many items a set has, use the len() method.
print(len(thisset))


"""
Set Items - Data Types
Set items can be of any data type:
String, int and boolean data types
"""
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)



#A set can contain different data types
#A set with strings, integers and boolean values
set4 = {"abc", 43, "male", "female", True, False}
print(set4)




#type() From Python's perspective, sets are defined as objects with the data type 'set'
myset = {"apple", "banana", "cherry"}
print(type(myset))



# set contructor
'''
# Note: the set list is unordered,
 so the result will display the items in a random order.
'''
thisset = set(("apple", "banana", "cherry"))
print(thisset)

