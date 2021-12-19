# Remove Item
# To remove an item in a set, use the remove()

thisset = {"apple","banana","cherry","orange"}
thisset.remove("banana")
print(thisset)
#Remove "banana" by using the discard() method
thisset.discard("orange")
print(thisset)



#Remove the last item by using the pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal



#The clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


'''
#The del keyword will delete the set completely
thisset1 = {"apple", "banana", "cherry"}
del thisset1
print(thisset1) #this will raise an error because the set no longer exists

'''
