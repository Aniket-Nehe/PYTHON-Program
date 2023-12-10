# Python Set
# Unordered collection of various items enclosed within the curly braces. 
# The elements of the set can not be duplicate. 
# The elements of the python set must be immutable

#Creating Set in Python

print("-------------Creat Set={}------------")
set={1,4,2,5,7,2,6,7,9} #set return only unique element
print(set)
print()

#Creating Empty Set in Python
print("-------------Empty Set()------------")
# empty_set = set()
# print(empty_set)  # Output: set()
print()

# Adding and Removing Elements in Set:
print("---#-----#-----Adding and Removing Elements-----#-----#---")
my_set = {1, 2, 3, 4}  # Creating a set with unique elements
print(my_set)
print()

#add(element)
print("------------add()----------------")
my_set.add(5)  # Adding a single element to the set
print(my_set)  # Output: {1, 2, 3, 4, 5}
print()

#Update(itrable)
#iterable can be (list, tuple, set, etc.) 
print("------------update()----------------")
my_set.update({6, 7})  # Adding multiple elements using update(itrable)to the set.
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
print()

#remove(element)
# Removes the specified element from the set. Raises an error if the element is not present.
print("------------remove()----------------")
my_set.remove(3)# Removing an element from the set
# my_set.remove(13) # Raises an error because element is not present in set
print(my_set)  # Output: {1, 2, 4, 5, 6, 7}
print()

#discard(element):
# Removes the specified element from the set if it is present. Does not raise an error if the element is not found.
print("------------discard()----------------")
my_set.discard(3)  # Removing an element from the set
my_set.discard(13)  #Does not raise an error if the element is not found.
print(my_set)  # Output: {1, 2, 4, 5, 6, 7}
print()

#pop(element)
#  The pop() method removes and returns a random item from the set. Raises an error if the set is empty
print("------------pop()----------------")
modify=my_set.pop()  # Removing and return an random element from the set
print(modify) # Output: 1
print(my_set)# Output: {2, 5, 6, 7}


print()
print("---#-----#-----Copy and Clear method-----#-----#---")
print()

# Copy():
# The copy() method copies the set.
#  It returns a new set containing the same elements as the original set. Changes made to the original set after copying won't affect the copied set and vice versa.
print("------------copy()----------------")
original_set = {1, 2, 3, 4}
copied_set = original_set.copy()
original_set.add(5)# Modifying the original set

print("original_set : ",original_set)  # Output: {1, 2, 3, 4, 5}
print("copied_set : ",copied_set)    # Output: {1, 2, 3, 4}
print()


#Clear()
# The clear() method removes all elements from the set, making it an empty set.
print("------------clear()----------------")
my_set = {1, 2, 3, 4}
print("Before using clear() : ",my_set)  # Output: {1, 2, 3, 4}
my_set.clear()
print("After using clear() : ",my_set)  # Output: set()

print()
print("---#-----#-----Set operation-----#-----#---")
print()

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("set1=",set1)
print("set2=",set2)
print()

# Union (| or union() method):
# The union of two sets contains all unique elements from both sets.

print("------------Union (| or union() method)------------")
# Using the | operator:
union_set = set1 | set2 
print("Using the | operator:",union_set) # Output: {1, 2, 3, 4, 5, 6}
# Using union() method:
union_set = set1.union(set2)
print("Using union() method:",union_set)# Output: {1, 2, 3, 4, 5, 6}
print()

# Intersection (& or intersection() method):
# The intersection of two sets contains elements common to both sets.
print("------------Intersection (& or intersection() method)------------")
# Using the & operator:
intersection_set = set1 & set2
print("Using the & operator:",intersection_set) # Output: {3, 4}
# Using intersection() method:
intersection_set = set1.intersection(set2)
print("Using intersection() method:",intersection_set) # Output: {3, 4}
print()

# Difference (- or difference() method):
# The difference between two sets contains elements present in the first set but not in the second.
print("------------Difference (- or difference() method)------------")
# Using the - operator:
difference_set = set1 - set2  
print("Using the - operator:",difference_set)# Output: {1, 2}
# Using difference() method:
difference_set = set1.difference(set2) 
print("Using difference() method:",difference_set)# Output: {1, 2}
print()


# Symmetric Difference (^ or symmetric_difference() method):
# The symmetric difference contains elements present in either set, but not in both.
print("------------Symmetric Difference (^ or symmetric_difference() method)------------")
# Using the ^ operator:
symmetric_difference_set = set1 ^ set2 
print("Using the ^ operator:",difference_set) # Output: {1, 2, 5, 6}
# Using symmetric_difference() method:
symmetric_difference_set = set1.symmetric_difference(set2) # Output: {1, 2, 5, 6}
print("Using symmetric_difference() method:" ,symmetric_difference_set)
print()


# difference_update() Method:
# difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
print("---------------difference_update() Method--------------")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print("setA=",setA)
print("setB=",setB)
# difference_update() Method:
setA.difference_update(setB)
print(" After difference_update() Method: ",setA) # Output: {1, 2}
print()

# symmetric_difference_update() Method:
# The symmetric_difference_update() method updates the set with elements that are present in either set but not in both.
print("---------------symmetric_difference_update() Method--------------")
setX = {1, 2, 3, 4}
setY = {3, 4, 5, 6}
print("setX= ",setX)
print("setY= ",setY)
# symmetric_difference_update() Method
print("Before symmetric_difference_update",setX)
setX.symmetric_difference_update(setY)
print("After symmetric_difference_update",setX)

print()
print("---#-----#-----Subset and Superset Concept: -----#-----#---")
print()

#subset (issubset())
# For two sets A and B, if every element in set A is present in set B, then set A is a subset of set B(A ⊆ B) and B is the superset of 
# set A(B ⊇ A).
print("---------------issubset() Method--------------")
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
subset_check = A.issubset(B) #Check if one set is a subset of another.
print(subset_check)  # Output: True
print()

#Superset (issuperset())
# In set theory, a superset is the opposite concept of a subset. If set (A) contains every element of set (B), and possibly more elements, then (A) is considered a superset of (B).
print("---------------issuperset() Method--------------")
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
superset_check = A.issuperset(B)
print(superset_check)  # Output: True
print()

#Disjoint Sets(isdisjoint())
# Two sets are disjoint sets if there are no common elements in both sets.
print("---------------issuperset() Method--------------")
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

disjoint_check1 = set1.isdisjoint(set2)
disjoint_check2 = set1.isdisjoint(set3)

print(disjoint_check1)  # Output: True (no common elements between set1 and set2)
print(disjoint_check2)  # Output: False (set1 shares elements with set3)



