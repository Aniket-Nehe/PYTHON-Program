# List Comprehension:
# List comprehension is a concise way to create lists in Python. It allows you to create a new list by specifying the elements you want to include, often in a single line of code

#Create list using for loop
l=[f'{i}'for i in range(10)]
print(l)

#eg2
h_letters = [ letter for letter in 'Aniket' ]
print( h_letters)

#If 
l=[f'{i}'for i in range(10) if i%2==0]
print(l)

#if-else
l=[f'{i} is Even' if i%2==0 else f'{i} is Odd' for i in range(10) ]
print(l)

#Nested if 
l=[f'{i}' for i in range(100) if i%2==0 if i%5==0]
print(l)


print()
print()
print("-----------------------------'Dictionary'---------------------------------------------")

#Create list using for loop
l={f'{i}:{i+2}'for i in range(10)}
print(l)

#If 
l={f'{i}:{i+2}'for i in range(10) if i%2==0}
print(l)

#if-else
l={f'{i}:{i+2}' if i%2==0 else f'{i}:{i+2}' for i in range(10)}
print(l)

#Nested if 
l={f'{i}:{i+2}' for i in range(100) if i%2==0 if i%5==0}
print(l)
