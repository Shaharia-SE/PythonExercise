#The union() method returns a new set with all items from both sets
set1 = {"Rony","Jony","Any","Kony"}
set2 = {1, 2, 3, 4}
set3 = set1.union(set2)
print(set3)


#The update() method inserts the items in set2 into set1
set1 = {"Rony","Jony","Any","Kony"}
set2 = {1, 2, 3, 4}
set1.update(set2)
print(set1)


'''
Keep ONLY the Duplicates
The intersection_update() method will 
keep only the items that are present in both sets.
'''

set1 = {"apple","banana","orange"}
set2 = {"mango","apple","kiwi"}
set1.intersection_update(set2)
print(set1)

#Return a set that contains the items that exist in both set

set1 = {"apple","banana","orange"}
set2 = {"mango","apple","kiwi"}
set3 = set1.intersection(set2)
print(set3)


"""
Keep All, But NOT the Duplicates
The symmetric_difference_update() method will 
keep only the elements that are NOT present in both sets.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)



#Return a set that contains all items from both sets, except items that are present in both:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
