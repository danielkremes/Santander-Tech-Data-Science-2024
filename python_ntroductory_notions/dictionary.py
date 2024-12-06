# Working with dictionaries
dictionary = {}

# Dictionary no value
dictionary_empty = dict() 

# Dictionary with value (Keys, Values)
dictionary = {'name':'Daniel','age':24,'occupation':'interneship'}

for x in dictionary.values():
    print(x)
print()

dictionary_empty["name"] = "Jose"
dictionary_empty['height'] = 1.80
dictionary_empty['age'] = 24

for x in dictionary_empty.items():
    print(x)

# Figure-out key in dictionary
print("last_name" in dictionary_empty) 
print("age" in dictionary_empty) 