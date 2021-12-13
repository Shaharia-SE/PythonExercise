# To change the value of a specific item, refer to the index number

Thislist = ["apple", "banana", "cherry","lemon","lichy","orange","mango","grape"]
Thislist[1] = "blackcurrant"
print(Thislist)

#Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
Thislist[1:4] = ["paypia","kul","tometo"]
print(Thislist)


#The insert() method inserts an item at the specified index:

Thislist.insert(1,"Batabilebu")
print(Thislist)