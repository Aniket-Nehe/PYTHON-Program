#star pattern using for loop
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()
    
    
#star pattern using for loop
for i in range(6, 0, -1):
    for j in range(1,i+1):
        print("*", end="")  #print any symbol change in "*" to "symbol"
    print()
