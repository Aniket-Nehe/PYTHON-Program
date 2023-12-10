#num pattern Using for loop
num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
# reverse num pattern using for loop 
print()
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
#1
# 12
# 123
# 1234
# 12345 
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()