class Parent:
    def __init__(self):
        print("This is parent class")
    def parents(self):
        print("Parents Method")
        
class brother(Parent):
    def __init__(self):
        super().__init__()
        print("This is brother class")
    def bro(self):
        print("Bro Method")

class sister(Parent):
    def __init__(self):
        super().__init__()
        print("This is sister class")
    def sis(self):
        print("sis Method")

s=sister()
s.parents()
# s.bro()
s.sis()
print("-------------------------")
b=brother()
b.parents()
b.bro()
# b.sis()
print("-------------------------")
p=Parent()
p.parents()
# p.bro()
# p.sis()
