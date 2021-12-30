# The local variable can be accessed from a function within the function:

def myfunction():
    x = 20
    print(x)

    def myinnerfunction():
        w = 30
        print(w)

    myinnerfunction()


myfunction()
