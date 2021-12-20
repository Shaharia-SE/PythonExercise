# You can loop through a dictionary by using a for loop

thisdict =	{
  "brand": "Toyota",
  "model": "szwl",
  "year": 1964
}
for x in thisdict:
    print(x)


# Print all values in the dictionary, one by one
thisdict = {
    "brand": "Toyota",
    "model": "szwl",
    "year": 1964
}
for x in thisdict:
    print(thisdict[x])


# You can also use the values() method to return values of a dictionary
thisdict = {
    "brand": "Toyota",
    "model": "szwl",
    "year": 1964
}
for x in thisdict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary
thisdict = {
    "brand": "Toyota",
    "model": "szwl",
    "year": 1964
}
print("print Key method")
for x in thisdict.keys():

    print(x)

# Loop through both keys and values, by using the items() method

thisdict = {
    "brand": "Toyota",
    "model": "szwl",
    "year": 1964
}

for x, y in thisdict.items():
    print(x, y)