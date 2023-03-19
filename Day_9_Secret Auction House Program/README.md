# Secret Auction House Program
## Aim: Dictionary

## Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:

### Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
```
#Edit an item in dictionary
programming_dictionary["Bug"] = "A Month in your computer"

```

### Dictionary Items - Data Types
The values in dictionary items can be of any data type:
```
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
```

### type()
From Python's perspective, dictionaries are defined as objects with the data type 'dict':
```
<class 'dict'>
```

### Python Collections (Arrays)
There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.
- When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
```
# Using the dict() method to make a dictionary

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```
### Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:
```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
```
There is also a method called get() that will give you the same result:
```
x = thisdict.get("model")
```

### Get Keys
The keys() method will return a list of all the keys in the dictionary.
```
x = thisdict.keys()
```

### Get Values
The values() method will return a list of all the values in the dictionary.
```
x = thisdict.values()
```

### Get Items
The items() method will return each item in a dictionary, as tuples in a list.
```
# Get a list of the key:value pairs
x = thisdict.items()
```

### Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:
```
# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
```

### Changes Values
You can change the value of a specific item by referring to its key name:
```
# Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
```

### Update Dictionary
- The update() method will update the dictionary with the items from the given argument.
- The argument must be a dictionary, or an iterable object with key:value pairs.
```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
```
