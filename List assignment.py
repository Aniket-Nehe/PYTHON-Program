list=[45,71,22,9,19,37,99,99,81,25]
odd_list=[]
Even_list=[]

for i in list:
    if i%2==0:
        Even_list.append(i)
    else:
        odd_list.append(i)

print("Odd_List  : ",odd_list)
print("Even_List : ",Even_list)