# Range() Function
#syntax
#range(Start ,end ,step)

#print 1 to 10 using range  function
num=range(1,10)
print(num)
l=list(num) #range object is converted into list
print(l)

#print 1 to 10 reverse using range  function
num=range(10,0,-1) #start=10,stop=0,step=-1
print(num)
l=list(num) #range object is converted into list
print(l)