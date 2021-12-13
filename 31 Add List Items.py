#Append Items
#Using the append() method to append an item

Thislist = ["apple", "banana", "cherry"]
Thislist.append("orange")
print(Thislist)


'''
To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index
'''

Thislist.insert (1,"Lemon")
print(Thislist)

'''
Extend List
To append elements from another list to the current list, use the extend() method.
Example
Add the elements of tropical to thislist
'''

Thislist = ["apple", "banana", "cherry"]
Seconlist = ["mango", "pineapple", "papaya"]
Thislist.extend(Seconlist)
print(Thislist)

#Add elements of a tuple to a list
thislist = ["apple", "banana", "cherry","Tomato","Potato"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)