#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(7,9))

#Summarize argument a, b, and c and return the result:

x = lambda a, b, c: a + b + c
print(x( 2, 3, 4))


#Use that function definition to make a function that always doubles the number you send in:

def myfunction (n):
    return lambda a : a *n
x = myfunction(5)
print(x(20))

#Or, use the same function definition to make both functions, in the same program


def myfunction (n):
    return lambda a : a *n
x = myfunction(5)
x = myfunction(10)
x = myfunction(20)
print(x(20))
print(x(30))
print(x(40))