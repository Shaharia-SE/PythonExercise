# If statement
a = 30
b = 100
if b > a :
    print("b is grater than a")


# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 10
b = 10
if a > b :
    print("a is grater than b")
elif a == b :
    print("a and b are equal")

a = 100
b = 100
if a > b :
    print("a is grater than b")
elif b > a :
    print("b is grater than a")
else:
    print("a and b are equal")

#Short Hand If
if a > b: print("a is greater than b")


# Short Hand If ... Else

a = 2
b = 330
print("A") if a > b else print("B")

a = 2
b = 330
print("A") if a > b else print("B")



#And
#The and keyword is a logical operator, and is used to combine conditional statements

a = 100
b = 50
c = 300
if a > b and c > b:
    print(" both condition are true")


#or
#The or keyword is a logical operator, and is used to combine conditional statements
a = 100
b = 50
c = 300
if a > b or c > b:
    print(" At list one condition are true")


#Nested If
#You can have if statements inside if statements, this is called nested if statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



#The pass Statement
a = 33
b = 200

if b > a:
  pass
print("pass")
# having an empty if statement like this, would raise an error without the pass statement