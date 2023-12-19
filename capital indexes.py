#using function

def capital_indexs (s):
    index=[]
    for i in s:
        if i.isupper():
            res=(s.index(i))
            index.append(res)
    print(index)
capital_indexs("HeLlO")            

print("================================================================")
#Using List comprehension:  
def capital_indexs(s):
     return[i for i in range (len(s)) if s[i].isupper()]
print(capital_indexs("TNsT"))

    