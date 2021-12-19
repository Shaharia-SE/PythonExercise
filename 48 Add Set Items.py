# Add an item to a set, using the add() method
thisset = {"apple","banana","cherry","orange"}
thisset.add("kiwi")
print(thisset)

'''
To add items from another set into the current set, use the update() method
'''

set1 = {"apple","banana","cherry"}
set2 = {"orange","kiwi","papiya"}
set1.update(set2)
print(set1)



# Add Any Iterable
thisset = {"apple","banana","cherry"}
mylist = ["mango","lemon","orange"]
thisset.update(mylist)
print(thisset)