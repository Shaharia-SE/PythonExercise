# Create a variable outside of a function, and use it inside the function
X= "Shaharia Safat Rony"
def myfunction():
    print("This call " + X)
myfunction()

#Create a variable inside a function, with the same name as the global variable
A = "This is global variable"
def myfunction1():
    A = "This is Local variable"
    print(A)
myfunction1()
print(A)
# use the global keyword
def function2():
    global X
    X= "Awesome"
function2()
print("Global function is " + X)
#change the value of a global variable inside a function
B = "Rony"
def function3():
    global B
    B = "Shaharia Rony"
function3()
print(B)
