#1.Write a Python program that prints (as a list) the elements of listA that are not in listB as a list.
#If the lists have the same elements, print an empty list.
#If listA is an empty list, print an empty list.
listA=[1,2,3,4,"Aniket","Aditya",45]
listB=[1,2,3,4,"Aniket"]
res=[]
for i in listA:
    if listA in listB:
        print("Empty List")
    elif i not in listB:
        res.append(i)
print("#1 : ",res)
print()

# 2.Write a Python program that calculates the distance between two 3D points.
# The points are represented by two lists with three elements. The first element is the x-coordinate. The second element is the y-coordinate. The third element is the z-coordinate.
l1=[1,2,3]
l2=[4,5,6]
dist=((l2[0]-l1[0])**2 + (l2[1]-l1[1])**2 + (l2[2]-l1[2])**2 )**0.5
print("#2 : ",dict)
print()



#3.Write a Python program that prints the second largest value in a list.
# If the list is empty or only has one element, print None.
#1
l=[1,2,3,4,7,8,9,8,7,9]
x=set(l)
y=list(x)
y.sort()
print( "#3 : ",y[-2])

#2
l=[1,2,3,4,7,8,9,8,7,9]
l.sort()
if len(l)==0 or len(l)==1:
    print("None")
elif l[-1]==l[-2]:
    print("#3.1 :",l[-3])
else:
    res=l[-2]
    print("#3.1 :",res)
print()
#4. Write a Python program that prints the elements of a list on the same line.
# The elements should be separated only by a space (not by a comma).
# The output should not include the opening and closing square brackets [ ].

list1=[1,9,2,8,3,7,4,5,6]
print("#4 : ", end=" ")
for i in list1:
    print(i,end=" ")
print()
print()

#5.  Write a Python program that prints the largest and smallest values in a list
# Print the two values on the same line, separated by a space.
# The largest value should appear first and the smallest value should appear second.
# You may assume that the list only contains numeric values.
# If the list is empty, print None.

#using min() max() function
lst=[23,54,34,56,23,7,9,67,45]
if len(lst)==0 or len(lst)==1:
    print("Empty List")
else:
    min=min(lst)
    max=max(lst)
    print("#5 : ",max,min ,sep=" ")

#using sort()
lst=[23,54,34,56,23,7,9,67,45]
lst.sort()
if len(lst)==0 or len(lst)==1:
    print("Empty List")
else:
    print("#5.1 : ",lst[-1],lst[0],sep=" ")
print()
#6 .Write a Python program that multiplies all the items in a list by the value of the variable factor.
# The program must print the list as the output.
# The program should also allow multiplying the variable factor by a string in case the list contains strings.
# You may assume that the value of factor will be a positive integer.
lst=[5,7,3,5,2,3,6]
factor=2 #int(input("Enter the Factor : "))
res=[]
for i in  lst:
    res.append(i*factor)
print("#6 : ",res)
print()

# 7.Write a Python program that checks if a list is empty or not.
# If the list is empty, print "Empty". Else, print "Not Empty"
lst=[5,7,3,5,2,3,6]
if len(lst)==0:
    print("#7 : Empty")
else:
    print("#7 : Not Empty")  
print()

# 8: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
lst=[5,7,3,5,2,3,6]
square=[]
for i in lst:
    square.append(i**2)
print("#8 : ",square)
print()
# 9: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res=[]
for i in list1:
    for j in list2:
        res.append(i+j)
print("#9 : ",res)
print()

#  10:Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res=[]
for i in list1:
    if len(i)>1:
        res.append(i)
print("#10 : ",res)
print()

# 11.Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print("#11 : ",list1)
print()

# 12 Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
# Given List:
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # sub list to add
# sub_list = ["h", "i", "j"]
# Expected Output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

