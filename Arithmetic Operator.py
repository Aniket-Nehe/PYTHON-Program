# 1. Arithmetic Operator:
# Q1. Create a program that takes two numbers as input and prints their sum.
num1=int(input("Enter The First Number : "))
num2=int(input("Enter The Second Number : "))
addition=num1+num2
print("Q1 : Addition is = ",addition)
print()

# Q2. Write a program that subtracts the second number from the first. Take these two numbers as input.
Subtraction=num1-num2
print("Q2 : Subtraction is = ",Subtraction)
print()

# Q3.Create a program that multiplies two numbers taken as input.
Multiplication=num1*num2
print("Q3 : Multiplication is = ",Multiplication)
print()

# Q4. Write a program that divides the first number by the second (non-zero) number. Take these two numbers as input.
Division=num1/num2
print("Q4 : Division is = ",Division)
print()

# Q5. Create a program that performs floor division on two numbers. Take these two numbers as input.
Floor_Division=num1//num2
print("Q5 : Floor_Division is = ",Floor_Division)
print()

# Q6. Write a program that calculates the remainder when the first number is divided by the second (non-zero) number. Take these two numbers as input.
Modulus=num1%num2
print("Q6 : Reminder is = ",Modulus)
print()

# Q7.Create a program that calculates the result of raising the first number to the power of the second number. Take these two numbers as input.
power=num1**num2
print("Q7 : Power is = ",power)
print()

# Q8.Write a program that calculates compound interest. Take the principal amount, rate of interest, and time as input.
principal_amount=int(input("Enter The Amount : "))
rate_of_interest=float(input("Enter Rate Of Intrrest : "))
time=float(input("Enter Time In Year : "))

amount=principal_amount*(1+(rate_of_interest/100))**time  # formula for calculating amount 
compound_interest = amount - principal_amount
print("Q8 : compound_interest : ",compound_interest )
print()

# Q9.Create a program that takes a number as input, increments it, and then decrements it. Print both the incremental and decremental values.
increment=num1+1
decrement=num1-1
print("Q9 : increment ",increment)
print("   : decrement ",decrement)
print()

# Q10.Write a program that takes three numbers as input and calculates their average.
num3=int(input("Enter Third Number : "))
average=(num1+num2+num3)/3
print("Q10 : Average is : ",average)