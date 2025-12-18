# Dictionaries are used to store data values in key:value pairs

# “key” : value

# They are unordered, mutable(changeable) & don’t allow duplicate keys

dictionary1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "subjects": ["Math", "Science", "Art"],
    "tuple_data": (1, 2, 3)

}

print("Original dictionary:", dictionary1["name"])  # Output: Original dictionary: Alice

# Modifying a value

dictionary1["age"] = 31
print("Updated age:", dictionary1["age"])  # Output: Updated age: 31
# Adding a new key-value pair
dictionary1["profession"] = "Engineer"
print("Added profession:", dictionary1)  # Output: Added profession: Engineer



#Nested Dictionaries

dictionary2 = {
    "person1": {
        "name": "Bob",
        "age": 25
    }
}
print("Nested dictionary:", dictionary2)


#Dictionary Methods

myDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

#returns all keys
print(myDict.keys())

#returns all values
print(myDict.values())


 #returns all (key, val) pairs as tuples
print(myDict.items())

#get value of specified key
print(myDict.get("model"))  # Output: Mustang



myDict.update({"new brand":"bmw"})  #inserts the specified items to the dictionary

print(myDict)

newdict = myDict
del myDict  #removes the dictionary completely
print(newdict)