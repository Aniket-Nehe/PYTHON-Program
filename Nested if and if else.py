#Nested if
#check user can eligible for vote using nested if 
age=int(input("Enter your Age"))
country=input("Enter Country Name")
if(age>18):
    if(country=="india"):
        print("You can Vote")
else:
    print("You can't Vote")
    
#Nested if Else
#check number is negative,positive or zero
num=int(input("Enter The Number"))
if(num<0):
    print("Number is negative")
else:
    if(num>0):
        print("Number is positive")
    else:
        print("Number Is Zero")