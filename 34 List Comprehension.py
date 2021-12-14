
'''Without list comprehension you will have to write
a for statement with a conditional test inside:'''

fruits = ["apple", "banana","cherry","kiwi","mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


#With list comprehension you can do all that with only one line of code
newlist = [x for x in fruits if "b" in x]

print(newlist)


#The condition is like a filter that only accepts the items that valuate to True

print("Conditional")
newlist = [x for x in fruits if x != "apple"]
print(newlist)

'''
Example
With no if statement
'''

newlist = [x for x in fruits]
print(newlist)

#You can use the range() function to create an iterable
newlist = [ x for x in range(10)]
print(newlist)

#Accept only numbers lower than 5:
newlist = [ x for x in range(10) if x < 5]
print(newlist)

#Set the values in the new list to upper case
newlist = [x.upper() for x in fruits]
print(newlist)

print(" Set all values in the new list to 'tometo':")
newlist = ['tomato' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)