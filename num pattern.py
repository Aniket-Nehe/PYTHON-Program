# Write a program to display the following pattern using nested loops.

# 1                                                                  
# 22                                                             
# 333                                                       
# 4444                                                    
# 55555         
for i in range(1,5+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


print("----------------------------------------")
# 1                                                                  
# 22                                                             
# 333                                                       
# 4444                                                    
# 55555

for i in range(1,5+1):
    for j in range(i):
        print(i,end="")
    print()    