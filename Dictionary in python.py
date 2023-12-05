# Dictionary:
# A dictionary in Python is an unordered collection of key-value pairs. 
# Each key must be unique, and it is associated with a corresponding value. 
# The keys are the immutable python object, i.e., Numbers, string or tuple.
# Dictionaries are created using curly braces {} or the dict() constructor. 

#Creating Dictionary in Python
print("-------------Creat dictionary------------")
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'} #set return only unique element
print(my_dict)
print()

#Creating Empty Dictionary in Python
print("-------------Empty Set()------------")
empty_dict = {}
print(empty_dict)
print()

print()
print("---#-----#-----Dictionary method-----#-----#---")
print()

#clear():
# The clear() method removes all items from a dictionary. After using clear(), the dictionary becomes empty.
print("-------------Clear()------------")
my_dict = {"a": 1, "b": 2}
my_dict.clear() # Output: {}
print()

#Copy():
# The copy() method in Python is used to create a shallow copy of a dictionary
print("-------------Copy()------------")
my_dict = {"a": 1, "b": 2}
new_dict = my_dict.copy() 
print("Orignal_Dict : ",my_dict)  # Output: Orignal_Dict :  {'a': 1, 'b': 2}
print("New_Dict : ",new_dict)     # Output: New_Dict :  {'a': 1, 'b': 2}
print()

# get():
# The get() method retrieves the value associated with a specified key. It provides a way to safely access dictionary elements without raising a KeyError if the key is not present. 
print("-------------Get(key,default)------------")
my_dict = {"a": 1, "b": 2}

print(my_dict.get("a"))    # Output: 1
print(my_dict.get('x'))    # Output: None
print(my_dict.get('x',100))# Output: 100
print()

#items():
# The items() method returns a view of the dictionary's key-value pairs as tuples. Each tuple contains a pair of the key and its corresponding value.
print("-------------iteme()------------")
my_dict = {"a": 1, "b": 2}
items = my_dict.items()
print(items) # Output: dict_items([('a', 1), ('b', 2)])
print()

#key():
# The keys() method displays a list of all the keys in a dictionary.
print("-------------keys()------------")
my_dict = {"a": 1, "b": 2}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b'])
print()

#values():
# The values() method displays a list of all the values in a dictionary.
print("-------------values()------------")
my_dict = {"a": 1, "b": 2}
values = my_dict.values()
print(values)  # Output: dict_values([1, 2])
print()

#pop():
# The pop() method removes and returns the value associated with a specified key from a dictionary. If the key is not found, it raises a KeyError or returns a specified default value if provided.
print("-------------pop(key, default=None)------------")
my_dict = {"a": 1, "b": 2}
value = my_dict.pop("a")
print(value) # Output: value is 1, and my_dict becomes {'b': 2}
print()

#popitem():
# The popitem() method removes and returns the last key-value pair from the dictionary as a tuple.
print("-------------popitem()------------")
my_dict = {"a": 1, "b": 2}
item = my_dict.popitem()
print("item is ",item)# Output: item is ('b', 2), and my_dict becomes {'a': 1}
print() 

#update():
# The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary, or an iterable object with key value pairs.
# If a key already exists in the original dictionary, its value is updated; otherwise, a new key-value pair is added.
print("-------------update()------------")
my_dict = {"a": 1, "b": 2}
my_dict.update({"c": 3})
print(" my_dict becomes ",my_dict)# Output: my_dict becomes {'a': 1, 'b': 2, 'c': 3}
print()

#setdefault():
# setdefault() method gets the value of a key from a dictionary. If the key is present in the dictionary, it returns the corresponding value. If the key is not present, it inserts the key with a specified default value and returns that value.
print("-------------setdefault()------------")
my_dict = {"a": 1, "b": 2}
print(my_dict.setdefault("b"))  # Output: 2
print(my_dict.setdefault("f"))  # Output: None
my_dict.setdefault("c", 3)
print("my_dict becomes", my_dict)  # Output: my_dict becomes {'a': 1, 'b': 2, 'c': 3}
print()

#formkeys():
# The fromkeys() method creates a new dictionary with keys from a given iterable and values set to a default value.
# Here, iterable is the iterable (list, tuple, etc.) from which keys will be taken, and value is the default value to be set for all keys. If value is not provided, it defaults to None.
print("-------------setdefault(iterable, value)------------") 
new_dict = dict.fromkeys(['a', 'b', 'c'])
print(new_dict) # Output: {'a': None, 'b': None, 'c': None}

# Creating a dictionary with a specified default value
new_dict_with_value = dict.fromkeys(['a', 'b', 'c'], 100)
print(new_dict_with_value) # Output: {'a': 100, 'b': 100, 'c': 100}

print()