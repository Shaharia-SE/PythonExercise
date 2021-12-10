'''age = 36
txt = "My name is John, I am " + age
print(txt) #we cannot combine strings and numbers like this'''
age = 24
txt = "My name is Rony, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} taka."
print(myorder.format(quantity, itemno, price))