#num pattern Using for loop
num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
# reverse num pattern using for loop 

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
#1 12 123 1234 12345 pattern
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()