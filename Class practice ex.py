# 1 .Greater Number :

'''x=int(input('enter the number: '))
y=int(input('enter the number: '))
z=int(input('enter the number: '))
n=int(input('enter the number: '))


if(x>y and x>z and x>n):
    print('x is the gretest')
elif(y>z and y>n):
    print('y is the gretest')
elif(z>n):
    print('z is the gretest')
else:
    print('n is the gretest')'''
    

# 2. write a program to print even number between 100 and 200 using while loop  
# print Even Number between 100 and 200 using while loop

'''print("----------------------output using While Loop-----------------")
num=100
i=1
while(num<=200):
    if num%2==0:
        print(num ,end=" ")
        num+=2
print()
print()


# print Even Number between 100 and 200 using for loop
print("-----------------output using For Loop-------------------------")
for i in range(100,200,2):
    print(i,end=" ")
'''

# 3. Write a program to find the prime number.

'''num=int(input("Enter the number : "))
if num > 1:
    for i in range(2,num):
        if(num%i==0):
            print("Not prime number")
            break
    else:
        print("prime number")
else:
    print("Not A prime number")'''
    
    
# 4. Write a Python program that prints the length of a string s.

'''str=input("Enter The String")
print((len(str)))'''


# 5. 5.Write a Python program that prints the character at index i in the string s. 
#If the index is out of range, the program should print "i is out of range".
#If the string is empty, the program should print "Empty String".

'''s=input("Enter The String : ")
i=int(input("Enter The Index : "))


if((len(s))<=0):
    print("Empty String")
elif(i>(len(s))):
    print("i is out of range")
else:
    print("character at index",i ,"is",s[i])
print("--------------------------------------------------")'''


# 6.Write a Python Program that prints the reversed version of a string. 
#The program must preserve uppercase and lowercase letters. If the string is empty, print it intact.

'''s=input("Enter The String : ")
if ((len(s))<=0):
    print("Empty String")
else:
    print("reverse str =",s[::-1])'''


# 7. Write a Python program that prints the first and last three characters of the string s as a single string. 
#If the string has less than six characters, print an empty string (blank output)

'''s=input("Enter string")
len=(len(s))
if(len<6):
    print()
else:
    start=s[:3]
    print(start)
    last=s[-3:]
    print(last)
print("-------------------------------------------------")'''


# 8. Write a Python program that prints the string s without the characters located at even indices.
#If the string is empty or only has one character, print it intact

'''#using slicing
str=input("Enter the string : ")
print(str[1::2])

#using for loop
str=input("Enter the string : ")
len=(len(str))
for i in range(1,len,2):
    print(str[i] ,end=" ")'''


# 9. Write a Program to print prime using return statement.

# 10. Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
#curr_char and new_char are variables that contain strings with a single character. 
# You may assume that new_char will not be an empty string.
#The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
#If no match is found, print the initial string

'''s=input("Enter the String : ")
curr_char=input("Enter current char : ")
new_char=input("Enter new char : ")
 
if new_char=="":
    print("Empty string")
else:
    print(s.replace(curr_char,new_char))'''
    
# 11. Write a Python program that check if a string only contains numbers. If it does, print True. Else, print False.

'''str=input("Enter the string : ")
if str.isdigit():
    print("True")
else:
    print("False")'''

# 12. Write a Python program that prints a version of the string s with all commas replaced by dot

'''str="Hello,python,this,is,replace."
print(str.replace(",","."))'''

# 13. Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").
# If it does, print True. Else, print False. Before comparing the characters, you should convert the string to lowercase.
# If the string contains spaces, ignore them before finding the result.
# You may assume that the string doesn't contain any other symbols, only spaces (possibly).
# Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz

'''import string
str=input("Enter The String : ")
l=set(str.lower())
r=l.remove(" ")
print(l == set(string.ascii_lowercase))'''


#14. write a Python program that prints a copy of the string s without any spaces using for loop.
#Words should be connected in the final string.
#If the string doesn't contain spaces, print it intact.
 
'''str=input("Enter The String : ")
for i in str:
    print(i.replace(" ","") ,end="")'''

#15. Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.

#If it does, print True. Else, print False.
#This test should be case sensitive. For example, "A" should not be equivalent to "a".
#If the length of the prefix is greater than the length of the string, print False.

'''Str=input("Enter The String : ")
pref=input("Enter The prefex : ")

if(Str.startswith(pref)):
    print("True")
elif (pref > Str):
    print("False")'''
    

#16. Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.
#If it does, print True. Else, print False.
#This test should be case sensitive. Therefore, "A" should not be equivalent to "a".
#If the length of the suffix is greater than the length of the string, print False.

'''Str=input("Enter The String : ")
Suff=input("Enter The Suffix : ")

if(Str.endswith(Suff)):
    print("True")
elif (Suff > Str):
    print("False")'''

#17. Write a Python program that reverses the individual words in the string s and changes their capitalization.
# Uppercase letters should be printed in lowercase and vice versa.

'''Str=input("Enter The String")
print(Str.swapcase())'''

#18.write a Python program that prints if a given year was (or will) be a leap year.

'''year=int(input("Enter The  Year"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"Is A Leap Year")
else:
    print(year,"is Not A Leap Year")'''


