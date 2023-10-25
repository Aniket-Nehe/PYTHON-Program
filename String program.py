#1.1.Write a Python program that prints the length of a string s.
'''str=input("Enter The String ")
print((len(str)))
print("--------------------------------------------------")'''

#3.Write a Python program that prints the first and last three characters of the string s as a single string.
#If the string has less than six characters, print an empty string (blank output)
'''s=input("Enter string : ")
len=(len(s))
if(len<6):
    print()
else:
    start=s[:3]
    print(start)
    last=s[-3:]
    print(last)
print("-------------------------------------------------")'''

#2.Write a Python program that prints the character at index i in the string s.
#If the index is out of range, the program should print "i is out of range"
#If the string is empty, the program should print "Empty String"

'''s=input("Enter The String : ")
i=int(input("Enter The Index : "))

if((len(s))<=0):
    print("Empty String")
elif(i>(len(s))):
    print("i is out of range")
else:
    print("character at index",i ,"is",s[i])
print("--------------------------------------------------")'''

#4.Write a Python Program that prints the reversed version of a string.
#The program must preserve uppercase and lowercase letters.
#If the string is empty, print it intact.
'''s=input("Enter The String : ")
if ((len(s))<=0):
    print("Empty String")
else:
    print("reverse str =",s[::-1])
print("--------------------------------------------------")'''

#5.Write a Python program that prints the string s without the characters located at even indices.
#If the string is empty or only has one character, print it intact

#using slicing
str=input("Enter the string : ")
print(str[1::2])
print("---------------------------------------------------")
#using for loop
str=input("Enter the string : ")
len=(len(str))
for i in range(1,len,2):
    print(str[i] ,end=" ")






    