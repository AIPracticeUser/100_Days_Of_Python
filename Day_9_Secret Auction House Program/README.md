# Secret Auction House Program
Silent Auction House which gets every person's name and bid amount and store them in a dictionary. 

The program will ask if there is any more bidder, press yes to contiune, no to finalize the auction bidding

The auction bidding will declare the winner with the bid amount

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

### Exercise 1
Solution link: https://replit.com/@LightGamer1/Day9Exercise-1?v=1

### Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
```
#Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
```
Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
```
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```

### Access Items in Nested Dictionaries
To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

```
print(myfamily["child2"]["name"])
```

### Python Dictionary Methods
- clear()	Removes all the elements from the dictionary
- copy()	Returns a copy of the dictionary
- fromkeys()	Returns a dictionary with the specified keys and value
- get()	Returns the value of the specified key
- items()	Returns a list containing a tuple for each key value pair
- keys()	Returns a list containing the dictionary's keys
- pop()	Removes the element with the specified key
- popitem()	Removes the last inserted key-value pair
- setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
- update()	Updates the dictionary with the specified key-value pairs
- values()	Returns a list of all the values in the dictionary

### Exercise 2 (Adding new travel log in the form of nested dictionaries in a list)
Working Solution: https://replit.com/@LightGamer1/Day9Exercise2?v=1

### Secret Auction House

Silent Auction House which gets every person's name and bid amount and store them in a dictionary. 
The program will ask if there is any more bidder, press yes to contiune, no to finalize the auction bidding
The auction bidding will declare the winner with the bid amount

Work Flow:


![image](https://user-images.githubusercontent.com/100339175/226159503-f802b0c2-0fca-4dfa-877f-16334f7ddee7.png)

Working Solution: https://replit.com/@LightGamer1/blind-auction-start?v=1



