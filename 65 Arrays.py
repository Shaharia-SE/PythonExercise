#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW","cw2"]
print(cars)

#Access the Elements of an Array

cars = ["Ford", "Volvo", "BMW","cw2"]
x = cars[1]
print(x)

#Modify the value of the first array item:

cars = ["Ford", "Volvo", "BMW","cw2"]
cars[0] = "Toyota"
print(cars)

#The Length of an Array

cars = ["Ford", "Volvo", "BMW","cw2","Toyota"]
x = len(cars)
print(x)

#Looping Array Elements
cars = ["Ford", "Volvo", "BMW","cw2","Toyota"]
for x in cars:
    print(x)


#Adding Array Elements


cars = ["Ford", "Volvo", "BMW","cw2","Toyota"]
cars.append("Honda")
print(cars)


#Removing Array Elements
cars = ["Ford", "Volvo", "BMW","cw2","Toyota"]
cars.pop(2)
print(cars)

cars = ["Ford", "Volvo", "BMW","cw2","Toyota"]
cars.remove("Volvo")
print(cars)