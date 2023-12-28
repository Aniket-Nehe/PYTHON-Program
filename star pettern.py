#star pattern using for loop
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()
    
print()
print("==============================================")

#star pattern using for loop
for i in range(6, 0, -1):
    for j in range(1,i+1):
        print("*", end="")  #print any symbol change in "*" to "symbol"
    print()
    
    
#squrea pattern 

print("==============================================")
#squrea pattern 

size = 5
for i in range(0, size):
    print("*" * size)
    
print("==============================================")
# hollow square pattern
size = 3
for i in range(size):
    if i == 0 or i == size - 1:
        print('* ' * size)
    else:
        print('* ' + '  ' * (size - 2) + '* ')
        
#Piramid
print("==============================================")
n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))