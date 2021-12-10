#using the type() function:
x=5
A = int(10)
print(type(x))
x = str("Hello Rony")
#display x:
print(x)
print(type(x)) #display the data type of x:
print(A)
print(type(A))
B= float(20.5) #float
print(B)
print(type(B))
C = complex(1j)    #complex
print(C)
print(type(C))
D = list(("apple", "banana", "cherry"))   #list
print(D)
print(type(D))
E =tuple(("apple", "banana", "cherry"))    #tuple
print(E)
print(type(E))
F = range(6)  #range
print(F)
print(type(F))
G = dict(name="John", age=36) # dict
print(G)
print(type(G))
H = set(("apple", "banana", "cherry")) #set
print(H)
print(type(H))
I = frozenset(("apple", "banana", "cherry")) #frozenset
print(I)
print(type(I))

J = bool(40) #bool
print(J)
print(type(J))
K = bytes(50) #bytes
print(K)
print(type(K))
L = bytearray(500) #bytearray
print(L)
print(type(L))
M = memoryview(bytes(50))   #memoryview
print(M)
print(type(M))