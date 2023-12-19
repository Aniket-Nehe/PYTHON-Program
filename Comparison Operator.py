# 2.Comparison Operator:
# Q1.Write a program to compare two numbers and print whether they are equal or not.
n1=100
n2=100
if n1==n2:
    print("Numbers Are Equal")
else:
    print("Number Are Not Equal")
print()

# Q2.Create a program that checks whether a given number is positive, negative, or zero.
num=int(input("Enter The Number: "))
if num < 0:
    print("Number is Negative")
elif num == 0:
    print("Number Is Zero")
else:
    print("Number Is  Positive")
print()

# Q3.Write a program to compare three numbers and find the maximum among them.
num1=int(input("Enter The First Number  : "))
num2=int(input("Enter The Second Number : "))
num3=int(input("Enter The Third Number  : "))
if (num1>num2)and(num1>num3):
    print("First Number ",num1,"Is Greather")
elif(num2>num1)and(num2>num3):
    print("Second Number ",num2,"Is Greather")
else:
    print("Third Number ",num3,"Is Greather")
print()

# Q4.Create a program to determine if a given year is a leap year or not.
year=int(input("Enter The Year : "))
if (year%100!=0 and year%4==0) or (year%400==0):
    print(year,"Is Leap Year")
else:
    print(year,"Is Not A leap Year")
print()

# Q5.Write a program to compare two strings and check if they are equal or not.
str1="Aniket"
str2="Aditya"
if str1==str2:
    print("Equal")
else:
    print("Not Equal ")
print()
    
# Q6.Create a program to determine whether a given number is even or odd.
n=int(input("Enter The Number "))
if n%2==0:
    print("Number is Even")
else:
    print("Number is Odd")
print()

# Q7.Write a program to check if a number is positive and even.
n1=int(input("Enter the Number : "))
if n1 > 1 and n1%2==0:
    print("Number is Positive And Even")
elif n1<0:
    print("Number is Negative")
else:
    print("Number is Odd")
print()

# Q8.Create a program to check if a number is divisible by another number.
num=int(input("Enter The Number : "))
div=int(input("Enter The Divide Number"))
if num%div==0:
    print(num,"Is Divisible by",div)
else:
    print(num,"Is Not Divisible by",div)


# Q9.Write a program to check if a given character is a vowel or consonant.
char=input("Enter The Character")
vovel="AEIOUaeiou"
if char in vovel:
    print("Charecter is Vovel")
else:
    print("Charecter is consonant")
print()
    
# Q10.Create a program to check if a number is greater than, less than, or equal to zero.
num=int(input("Enter The Number: "))
if num < 0:
    print("Number is less than Zero")
elif num == 0:
    print("Number Is equals to Zero")
else:
    print("Number Is  Greather than Zero")
print()

# Q11.Create a program to check if a number is positive and greater than 10.
n1=int(input("Enter the Number : "))
if n1 >=1 and n1>10:
    print("Number is Positive And greather than 10")
elif n1<0:
    print("Number is Negative")
else:
    print("Number is positive but less than 10")
print()

# Q12.Write a program to check if a number is odd and less than 100.
num=99
if num<=100 and num%2!=0:
    print("Number is less Than 100 And Odd")
elif num < 0:
    print("Number is Negative")
elif num >100:
    print("Number is Greather Than 100")
else:
    print("Number is Even")