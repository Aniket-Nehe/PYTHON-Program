#multi level inheritance
class GrandFather:
    def __init__(self) -> None:
        print("This is grandfather class.")
    def GFathername(self,name):
        self.name=name
        print(f"GrandFather Name is {self.name} ")
    
class Father(GrandFather):
    def __init__(self) -> None:
        super().__init__()
        print("This is father class.")
    def Fathername(self,name1):
        self.name1=name1
        print(f"Father Name is {self.name1} ")
        
class Son(Father):
    def __init__(self) -> None:
        super().__init__()
        print("This is son class.")
    def Sonname(self,name2):
        self.name2=name2
        print(f"Son Name is {self.name2} ")
        
s=Son()
s.GFathername("ABCD")
s.Fathername("EFGH")
s.Sonname("IJKL")
print("-----------------------------------------------")
f=Father()
f.GFathername("ABCD")
f.Fathername("EFGH")
f.Sonname("IJKL")
print("-----------------------------------------------")
g=GrandFather()
g.GFathername("ABCD")
g.Fathername("EFGH")
g.Sonname("IJKL")