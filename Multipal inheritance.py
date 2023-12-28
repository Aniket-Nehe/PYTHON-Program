class father:
    def __init__(self) -> None:
        print("This is father class.")
        
    def dad(self):
        print("Dad Method")

class Mother:
    def __init__(self):
        super().__init__()
        print("This is Mother Class")

    def mom(self):
        print("Mom Method")


class Child(Mother, father):
    def __init__(self):
        super().__init__() 
        print("This is Child class")
        
    def child(self):
        print("Child method.")

# Creating an object of the Child class
ch = Child()
ch.dad()    # Accesses dad method from father class
ch.mom()    # Accesses mom method from Mother class
ch.child()  # Accesses child method from Child class
print("-----------------------------")

# Creating an object of the Mother class
m = Mother()
# m.dad()   # There's no 'dad' method in the Mother class, so this line will raise an AttributeError
m.mom()     # Accesses mom method from Mother class
# m.child() # There's no 'child' method in the Mother class, so this line will raise an AttributeError
print("-----------------------------")

# Creating an object of the father class
f = father()
f.dad()     # Accesses dad method from father class
# f.mom()   # There's no 'mom' method in the father class, so this line will raise an AttributeError
# f.child() # There's no 'child' method in the father class, so this line will raise an AttributeError
print("==========================================")

#Dimand problam in python
class A:
    def __init__(self) -> None:
        print("Class A")
class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("Class B")
class C(A):
    def __init__(self) -> None:
        super().__init__()
        print("Class C")
class D(B,C):
    def __init__(self) -> None:
        super().__init__()
        print("Class D")

d=D()