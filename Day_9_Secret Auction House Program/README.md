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
```
# Using the dict() method to make a dictionary

```
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```
