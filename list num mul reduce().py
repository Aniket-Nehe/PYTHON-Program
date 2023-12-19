# 1)write a program using function definition to print multiplication of all the numbers in a list.
from functools import reduce
num=[1,2,3,4,5]
x=reduce(lambda x,y:x*y,num)
print(x)
