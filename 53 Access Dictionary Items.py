
#Accessing Items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result
x = thisdict.get("model")
print(x)

#The keys() method will return a list of all the keys in the dictionary.

x = thisdict.keys()
print(x)


#Add a new item to the original dictionary, and see that the keys list gets updated as well:

Car ={
    "brand" : "Toyota",
    " model" : "xz4",
    "year" : 2020
}
x = Car.keys()
print(x) #before the change
Car["colr"] = "white"
x = Car.keys()
print(x)# after change





#The values() method will return a list of all the values in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()
print(x)


#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) # before change
car["year"] = 2020
x = car.values()
print(x)


#Add a new item to the original dictionary, and see that the values list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change



#The items() method will return each item in a dictionary, as tuples in a list

x = car.items()
print(x)




#Make a change in the original dictionary, and see that the items list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change





#Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change



#Check if "model" is present in the dictionary

if "model" in thisdict:
     print(thisdict)