#List items are indexed and you can access them by referring to the index number
Thialist=["apple", "banana","orange","lemon","guava","grape","lichi","papia"]
print(Thialist[2])
'''
Negative Indexing
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.
'''
print(Thialist[-3])

#Return the third, fourth, and fifth item:
print(Thialist[3:6])#'''Note: The search will start at index 2 (included) and end at index 6 (not included).'''

#This example returns the items from the beginning to, but NOT including, "kiwi"
print(Thialist[:2])


"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third
"""
print(Thialist[2:])

'''
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

'''
Check if Item Exists
To determine if a specified item is present in a list use the in keyword
'''

Thislist1 = ["apple", "banana", "cherry"]
if "apple" in Thislist1:
  print("Yes, 'apple' is in the fruits list")