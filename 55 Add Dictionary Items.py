# Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
thisdict["glass"] = "silicon"
print(thisdict)


# Add a color item to the dictionary by using the update() method:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
thisdict["glass"] = "silicon"
thisdict.update({"color2" : "blue"})
print(thisdict)