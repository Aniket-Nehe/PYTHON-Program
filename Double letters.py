#using function

def double_letters(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False
print(double_letters("nano"))

#using list comprehention : 
def double_letters(s):
    return (s[i] == s[i + 1] for i in range(len(s) - 1))
print(double_letters("nano"))