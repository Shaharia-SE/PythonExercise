fruits = ("apple","banana","cherry","orange","kiwi")
(A, B, C, D, E) = fruits
print(A)
print(B)
print(C)
print(D)
print(E)


#Using Asterisk*

fruits = ("apple","banana","cherry","orange","kiwi","strawberry","mango")
(a, b, c, *d) = fruits
print(a)
print(b)
print(c)
print(d)



print("*************anoher aways*************")
(a, b, *c, d) = fruits
print(a)
print(b)
print(c)
print(d)