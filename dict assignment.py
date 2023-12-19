# Write a program that has the dictionary of your friends’ names as keys and phone numbers as its values. 
# Print the dictionary in a sorted order.
# Prompt the user to enter the name and check if it is present in the dictionary. If the name is not present, then enter the details in the dictionary.


di = {"Pratik": 9878024352,"Aniket": 7822028785,"Suraj": 8698765051,"Aditya": 8765878343}
sorted_dict = dict(sorted(di.items()))
print(sorted_dict)
print()
name = input("Enter the name to check: ")
if name in di:
    print(f"{name}:{di[name]}")
else:
    phone_number = input(f"Enter the phone number for {name}: ")
    new=di.setdefault(name,phone_number)
    print(name,new)
sorted_updated_dict = dict(sorted(di.items()))
print(sorted_updated_dict)
