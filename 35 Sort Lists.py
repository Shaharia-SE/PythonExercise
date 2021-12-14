
#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("Sort list")
print(thislist)

#Sort the list numerically:
thislist = [100,10,30,0,90,150,100,200]
thislist.sort()
print(thislist)

'''
Sort Descending
To sort descending, use the keyword argument reverse = True:
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100,10,30,0,90,150,100,200]
thislist.sort(reverse= True)
print(thislist)

'''
Customize Sort Function
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first):
Example
Sort the list based on how close the number is to 50:
'''

def function(n):
    return abs(n-50)
thislist = [23,50,65,13,82,100]
thislist.sort(key=function)
print("Sort the list based on how close the number is to 50")
print(thislist)

#Case Insensitive Sort
'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)'''



thislist = ["banana","Orange","kiwi","cherry","Apple"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

print("Perform a case-insensitive sort of the list:")
thislist.sort(key=str.lower)
print(thislist)

print("Reverse the order of the list items:")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)