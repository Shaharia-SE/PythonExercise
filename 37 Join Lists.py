print("Join Two Lists")
list1 = [" Rony","jony","any","kony"]
list2 = [1,2,3,4,5]
list3 = list1 + list2
print(list3)

print("Use the append() method to add list2 at the end of list1")
for x in list2:
    list1.append(x)
print(list1)



print("Use the extend() method to add list2 at the end of list1")
list1.extend(list2)
print(list1)