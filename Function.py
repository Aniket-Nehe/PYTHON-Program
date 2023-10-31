# Defining Function without Parameter
print('------Defining Function without Parameter-------')

def addition():
    a=10
    b=20
    res=a+b
    print("Addition is = ",res)

addition()

# Defining Function with Parameter
print('------Defining Function with one Parameter-------')

x="FULL STACK DEVELOPMENT"
def course(y):
    print("Course Name is : ",y)
    
course(x)

# Defining Function with Parameter
print('--------Defining Function with Parameter-------')

def multipication(x,y):
    result=x*y
    print("Multiplication is = ",result)
    
multipication(5,5)

# Defining multiple function and callling in one function
print('---- Defining multiple function and callling in one function---')

def add(x,y):
    res=x+y
    print("Addition is =",res)
    
def sub(x,y):
    res=x-y
    print("Substraction is =",res)
    
def multi(x,y):
    res=x*y
    print("Multiplication is = ",res)
    
x=10
y=5

def calculate():
    add(x,y)
    sub(x,y)
    multi(x,y)
    
calculate()
    