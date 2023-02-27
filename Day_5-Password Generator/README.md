## Password Generator
- Aim: For loop and Range 

Instructions
The program will ask:

- How many letters would you like in your password?
- How many symbols would you like?
- How many numbers would you like?


The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

There are two versions. 
### Easy Version
Generate the password in sequence, password might look like this:
![image](https://user-images.githubusercontent.com/100339175/221462801-ac37e907-ec5f-4290-b9de-c6bd8abf4c67.png)

### Hard Version
In the advanced version of this project the final password does not follow a pattern.
![image](https://user-images.githubusercontent.com/100339175/221463080-c7e1f8e5-7ce4-4830-9210-c92aa75ecfdf.png)

## Learning
### For Loop
- A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
- Example
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
print(x)
```

### For Loop with Range
- The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
```
for x in range(6):
print(x)
```

### For Loop with Break
- With the break statement we can stop the loop before it has looped through all the items
- Example: Exit the loop when x is "banana"
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```