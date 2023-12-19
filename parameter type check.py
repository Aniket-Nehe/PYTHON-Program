def only_ints(x,y):
    if type(x)==type(y):
        return True
    else:
        return False
print(only_ints(10,"a"))
