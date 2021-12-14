

Thislist = ["apple", "banana", "cherry","Tomato","Potato"]
Thislist.remove("cherry")
print(Thislist)

Thislist = ["apple", "banana", "cherry","Tomato","Potato"]
Thislist.pop(1) #Remove the second item
print(Thislist)

Thislist = ["apple","jelly","watermelon","banana","cherry","lemon","kuli"]
Thislist.pop() # Remove the last item:
print(Thislist)

'''Remove Specified Index
The pop() method removes the specified index.'''
print("remove specific")
Thislist.pop(1)
print(Thislist)

print("The del keyword also removes the specified index:")
del Thislist[0]
print(Thislist)
'''
Clear the List
The clear() method empties the list.
The list still remains, but it has no content
'''
print("All clear ")
Thislist.clear()
print(Thislist)