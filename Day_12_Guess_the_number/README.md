# Guess the number game
## LESSON: LOCAL SCOPE vs GLOBAL SCOPE

A variable is only available from inside the region it is created. This is called scope.
### Local Scope 
- A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
Example
```
#A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc()

result: 300
```

```
#The local variable can be accessed from a function within the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

```

### Global Scope
- A variable created in the main body of the Python code is a global variable and belongs to the global scope.
- Global variables are available from within any scope, global and local.

```
A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)
```

```
If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)
```
