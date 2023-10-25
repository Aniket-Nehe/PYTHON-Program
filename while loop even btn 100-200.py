# print Even Number between 100 and 200 using while loop
print("--------------------------------output using While Loop----------------------------")
num=100
while(num<=200):
    if num%2==0:
        print(num ,end=" ")
        num+=2
print()
print()

# print Even Number between 100 and 200 using for loop
print("--------------------------------output using For Loop----------------------------")
for i in range(100,200,2):
    print(i,end=" ")