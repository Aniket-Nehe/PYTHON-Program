class Father:
    def __init__(self) -> None:
        super().__init__()
        print("This is father class.")
    
    def Fathername(self, name1):
        self.name1 = name1
        print(f"Father Name is {self.name1} ")
        
class Son(Father):
    def __init__(self) -> None:
        super().__init__()
        print("This is son class.")
    
    def Sonname(self, name2):
        self.name2 = name2
        print(f"Son Name is {self.name2} ")


s=Son()
s.Fathername("ABCD")
s.Sonname("WXYZ")
print("-----------------------------------------")
f=Father()
f.Fathername("ABCD")
f.Sonname("WXYZ")