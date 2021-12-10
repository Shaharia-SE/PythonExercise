#Loop through the letters in the word "Bangladesh":
for x in "Bangladesh":
  print(x)
# String Length
# To get the length of a string, use the len() function
a = "bangladesh"
print(len(a))


#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "Life is very beautiful"
print("life" in txt)

#Use it in an if statement:

txt = "Life is very beautiful"
if "Life" in txt:
  print("yes, 'life' is  present.")

#Check if NOT
#we can use the keyword not in.
txt = "Life is very beautiful"
print("rony" not in txt)

# print only if "expensive" is NOT present:

txt = "Life is very beautiful"
if "rony" not in txt:
  print("no, 'rony' is not present.")
