num=int(input("Enter Number"))
fact=1
if num<0:
    print("enter the positive number")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
    