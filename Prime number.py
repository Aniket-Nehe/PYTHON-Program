# write  a  program to check number prime or not
#Prime number
num=int(input("Enter the number : "))
if num > 1:
    for i in range(2,num):
        if(num%i==0):
            print("Not prime number")
            break
    else:
        print("prime number")
        

else:
    print("Not A prime number")
