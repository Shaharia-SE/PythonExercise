#using the type() function:
x=5
A = 10
print(type(x))
x = "Hello Rony"
#display x:
print(x)
print(type(x)) #display the data type of x:
print(A)
print(type(A))
B= 20.5 #float
print(B)
print(type(B))
C = 1j    #complex
print(C)
print(type(C))
D = ["apple", "banana", "cherry"]   #list
print(D)
print(type(D))
E = ("apple", "banana", "cherry") #touple
print(E)
print(type(E))
F = range(6)  #range
print(F)
print(type(F))
G = {"name" : "John", "age" : 36} # dict
print(G)
print(type(G))
H = {"apple", "banana", "cherry"} #set
print(H)
print(type(H))
I = frozenset({"apple", "banana", "cherry"}) #frozenset
print(I)
print(type(I))

J = True #bool
print(J)
print(type(J))
K = b"Hello" #bytes
print(K)
print(type(K))
L = bytearray(5)  #bytearray
print(L)
print(type(L))
M = memoryview(bytes(5))   #memoryview
print(M)
print(type(M))