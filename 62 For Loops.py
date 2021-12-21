
#Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Loop through the letters in the word "Shaharia":

for x in "Shaharia":
    print(x)


#With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#Using the range() function:

for x in range(6):
  print(x)


#Using the start parameter:

for x in range(2, 6):
  print(x)


#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)


#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #If the loop breaks, the else block is not executed.


#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#The pass Statement
for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement
