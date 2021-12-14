'''
Loop Through a List
You can loop through the list items by using a for loop:
'''
Thislist = ["apple","jelly","watermelon","banana","cherry","lemon","kuli"]
for x in Thislist:
    print(x)

#Loop Through the Index Numbers
    print("Use the range() and len() functions to create a suitable iterable")
for i in range(len(Thislist)):
    print(Thislist[i])
#Using a While Loop
print("You can loop through the list items by using a while loop")
i = 0
while i < len(Thislist):
    print(Thislist[i])
    i = i + 1
# Looping Using List Comprehension

print("A short hand for loop that will print all items in a list:")
[print(x) for x in Thislist]