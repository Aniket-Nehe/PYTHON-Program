def EMI_cal():
    p=float(input("enter Principal Amount : "))
    r=float(input("Enter The Rate  Of Intrest Rate in Per(%) : "))
    n=float(input("Enter The  Number of Months : "))
    
    EMI=p*r*(1+r)**n/((1+r)**n-1)
    print(f"Monthly EMI is : ₹{EMI:.2f}/-")
EMI_cal()