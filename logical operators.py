#logical operators

#logical AND
print(10<12 and 10==10) #T T =T
print(10<12 and 10==12) #T F =F
print(18<12 and 10==10) #F T =F
print(18<12 and 10==12) #F F =F
print(10<12 and 3)      #T E =E
print(10<12 and 3 and 12) #T E =E #In this E consider the last element as E
print("----------------------------------------------")

#Logical OR
print(10<12 or 10==10) #T T =T
print(10<12 or 10==12) #T F =T
print(18<12 or 10==10) #F T =T
print(18<12 or 10==12) #F F =F
print(10<12 or 3)      #T E =E
print(18<12 or 3)      #F E =E
print(18<12 or 3 or 12) #T E =E #In this E consider the first element a E


#logical NOT
