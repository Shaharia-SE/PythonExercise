#Loop Through a Tuple
#You can loop through the tuple items by using a for loop

thistuple = ("apple","banana","chery","kiwi")
for x in thistuple:
    print(x)



#se the range() and len() functions to create a suitable iterable
thistuple = ("apple","banana","chery","kiwi")
for i in range(len(thistuple)):
    print(thistuple[i])

#Using a While Loop
#Print all items, using a while loop to go through all the index numbers

print("while loop")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
