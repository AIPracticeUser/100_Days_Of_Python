# Debugging

A debugger is a program that can help you find out what is going on in a computer program. You can stop the execution at any prescribed line number, print out variables, continue execution, stop again, execute statements one by one, and repeat such actions until you have tracked down abnormal behavior and found bugs.

## Exercise
### 1
```
 def my_function():
   for i in range(1, 20):
     print(i)
     if i == 20:
       print("You got it")

```
- Problem detected: The for loop will not reach 20, hence the if statement will not be execute

### 2
```
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
```
- Problem detected: list index out of range, because index of list start from 0 to 5

### 3
```
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
```
- Problem detected: year 1994 will be excluded out unintentionally

### 4
```
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
```
- Problem detected: need to put f in front for f-string function

### 5
```
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```
- Problem detected: the word_per_page should be equal '=' instead  of '=='

### 6
```
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
```
- Problem detected: Indentation is incorrect with b_list.append and print()

### 7
```
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

```
- Problem detected: the if statement should be '==' instead of '='

### 8
```
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
```
-Problem detected: year input should be integer instead of string

### 9
```
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
```
-Problem detected: For seperate if else conditon, it should be "elif" , not "if"
