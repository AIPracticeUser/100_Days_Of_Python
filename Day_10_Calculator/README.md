# Calculator Program

## LESSON: Functions with Output and Docstring
### Functions with output
- The Python return statement is a special statement that you can use inside a function or method to send the function’s result back to the caller.
- A return statement consists of the return keyword followed by an optional return value.
- You can omit the return value of a function and use a bare return without a return value, the return value will be None.

```
# Example
>>> def get_even(numbers):
...     even_nums = [num for num in numbers if not num % 2]
...     return even_nums
...

>>> get_even([1, 2, 3, 4, 5, 6])
[2,4,6]
```

The list comprehension gets evaluated and then the function returns with the resulting list. 
 * Note that you can only use expressions in a return statement.
 
```
# Example with list comprehension
>>> def get_even(numbers):
...     return [num for num in numbers if not num % 2]
...

>>> get_even([1, 2, 3, 4, 5, 6])
[2, 4, 6]
```

### Returning Multiple Values
- You can use a return statement to return multiple values from a function. 
- To do that, you just need to supply several return values separated by commas.
```
import statistics as st

def describe(sample):
    return st.mean(sample), st.median(sample), st.mode(sample)
```

### Exercise 1: Days in month
- Calculate the number of days depends on the input year and month. If leap year, there's 29 days in Feb.

Solution link: https://replit.com/@LightGamer1/Day10Days-in-Month?v=1

### DocString
- Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.
- Different from comments, comments are descriptions that help programmers better understand the intent and functionality of the program. 

![image](https://user-images.githubusercontent.com/100339175/226173653-db9ca025-f242-424f-ab22-2d7396ec9c90.png)

- usage of .___doc___ to call out the docstring
```
print(square.__doc__)
```



