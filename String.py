#String:
#String is the collection of Characters.

#Defining String ""
#String is defined by enclosing characters in single quotation marks, double quotation marks.

# Eg.
print("----------------Defining String--------------------")
F_Name="Aniket"
L_Name='Nehe'
print(type(F_Name))
print(type(L_Name))
print()


#Defining Multiline string :
#A line string is defined by enclosing characters in triple quotation marks.
print("-----------------Defining Multiline string--------------")
str="""Python is easy to learn
it is Free and open Sourse.
it is portable"""
print(str,type(str))
print()


#len() function
#This function returns the number of characters in the string.
print("-----------------len() function---------------------")
Name='Aniket Nehe'
len=len(Name)

print("Totsl No of charectar",len)
print()
#Indexing:
#Python strings are stored in the order in which the characters appear, and those characters can be accessed by referencing their position in the string.
print("-----------------Indexing----------------------------")
str="Hello..!, My Name Is Aniket Nehe"
print(str[4])
print(str[-6])
print(str[30])
print()

#Slicing:
#Partial part of the string can be obtained by Slicing.
#syntax:

#string_name[start:end:step]

#Start is the starting index of the character  from which slicing starts.
#End is the end index of the character where slicing ends.
Name="Aniket Nehe"
print(Name[0:6:1])
print(Name[7::1])
print(Name[3:6:1])

#print Even index char
print(Name[::2])

#print Odd index char
print(Name[1::2])

#print string in reverse
print(Name[::-1])

#print Aniket in reverse
print(Name[5::-1])
print()


#Operators in String

print("---------------Operators in String-----------------------")
#Appending or concatenating string
# +: Plus operator is use to  concatenate (splice strings together)

str1="This is String 1 ,"
str2="This is String 2 ,"
str3="This is String 3 "

print(str1+str2+str3)
print()

# * :  asterisk character is use to repeat a string:,
x="Hello Python  "*5
print(x)
print()

#Membership Operators will let you test for sub-strings inside a string:

# in
#True if value/variable is found in the sequence
string="Hello Python"
print("llo" in string)
print("on" in string)
print("pyn" in string)
print()
# not in
string="Hello Python"
print("llo" not in string)
print("on" not in string)
print("pyn" not in string)


print('-------Accessing String Using for Loop------------')
# Accessing String Using For loop
x='Avengers'
for i in x:
    print(i)

print()

print('-----2nd Method-------')
for i in 'Avengers':
    print(i)

print()

'''print('------3rd Method------')
x='Avengers'
y=len(x)
for i in range(y):
    print(x[i])'''


print()

