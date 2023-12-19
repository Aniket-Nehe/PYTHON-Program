#create first Class
class Car:
    def __init__(self,name,price):
        print("HELLO PYTHON")
        self.name=name
        self.price=price
        
    def info(self,name,age):
        print("Car")
        self.name=name
        self.age=age

        
x=Car("BMW series 3",123456789)
print(x.name)
print(x.price)
print(x.info("Aniket",18))
print(x.name)
print(x.age)
