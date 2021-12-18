#Convert the tuple into a list to be able to change it

x = ("apple","banana","cherry","orange")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Items
#Convert the tuple into a list, add "orange", and convert it back into a tuple

thistuple = ("apple","banana","cherry","orange")
y = list(thistuple)
y.append("kiwi")
thistuple = tuple(y)
print(thistuple)

#Add tuple to a tuple
#Create a new tuple with the value "orange", and add that tuple


y = ("mango",)
thistuple += y
print(thistuple)
'''Note When creating a tuple with only one item,
 remember to include a comma 
after the item, otherwise it will not be identified as a tuple'''

#Remove Items
thistuple = ("apple","banana","cherry","orange")
y = list(thistuple)
y.remove("banana")
thistuple =tuple(y)
print(thistuple)
