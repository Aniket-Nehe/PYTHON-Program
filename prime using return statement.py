'''def prime():
    num=int(input("Enter the Number : "))
    
    if(num>0):
        for i in range(2,num):
            if(num%i==0):
                print("Number Not a Prime Number")
                return
        else:
            print(" Number is a Prime Number")
                
    else:
        print("Enter The Valid  number")
        
prime()'''

def is_prime(num):
    if num<0:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def prime():
    num=int(input("Enter the Number"))
    if num>0:
        if is_prime(num):
            print("Prime Number")
        else:
            print("Not A Prime Number")
    else:
        print("Enter The Valid Number")

prime()