# Access Tuple Items
thistuple = ("apple","banana","orange","kiwi","melon", "mango")
print(thistuple[2])


#Print the last item of the tuple:
print(thistuple[-1])


#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT includedprint(thistuple[2:5])
print(thistuple[2:5])

#This example returns the items from the beginning to, but NOT included, "kiwi"
print(thistuple[:4])


#This example returns the items from "cherry" and to the end:
print(thistuple[2:])



#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

print(thistuple[-4:-1])

#Check if Item Exists
#To determine if a specified item is present in a tuple use the in keyword

if "orange" in thistuple:
    print("yes apple is this tuple ")
else:
    print("No")