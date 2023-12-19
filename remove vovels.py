str1=input("Enter The String : ")
vovel="aeiou"
without_vovel=""
for i in str1:
    if i not in vovel:
        without_vovel+=i
        
print("String : ",str1)
print()
print("String Without Vovels : ",without_vovel)