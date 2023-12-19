def mid(mid):
    if len(mid)%2!=0:
        l=len(mid)//2
        res=int(l)
        return mid[res]
    else:
        return ""
        
print(mid("abcef"))