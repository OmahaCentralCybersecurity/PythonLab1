# PythonLabOne
Recapping Data Types, Operators, & While Loops

## :one: The while loop
while loops allow programmers to repeat a task as a long as a certain condition stays true.  

### Repeat 'n' times
```
exp = 6
total = 1
base = 4

while exp > 0: 
  total = total * base
  exp--

print("total is:", total)
  
```

### Repeat until something happens
```
keep_counting = "y'
count = 0

while keep_counting = "y":
  count+=1
  print("count is: ", count)
  keep_counting = input("Do you want count another? (y/n)": )
  
print("the end count is: ", count)
  
```

## :two: Data Types and Operators 

1. Strings `str`
2. Numeric `int`, `float`, `complex`
3. Boolean `bool`
4. Characters

The type can be tested by using `type(variable)`, Python returns the class (or type) that the data is a part of. 
```
>>> name = "Omaha Central"
>>> type(name)
<class 'str'>
```

This can be a helpful tool when debugging since the data types are explicitly declared by the user like they are in Java. 
```
>>> age = 160
>>> type(age)
<class 'int'>
```
### Type Conversions
Python is dynamically typed (Java is statically typed) meaning that we don't have to declare what data types we will be using.  Howerver, to make conversions between data types, Python has some helpful functions.  

- String to an int
```
>>> age = "31"  
>>> birth_year = 2020 - int(age)
>>> print(birth_year)
1989 
```
- Int to a string
```
>>> height = 77
>>> print("You are " + str(height) + " inches tall")
```

`float(x)` converts an int or a string that is a number to a floating point value.  

Conversions can also be used to convert float values to integers. In this case, the decimal is dropped, not rounded.  
Python will return a `ValueError` when try to convert data that can't be converted to another specified data type.  

### Operators 
Arithemtic Operators in Python: 

| Operator    | Description |
| --- | --- |
| + | addition |
| - | subtraction |
| * | multiplication|
| / | division (float) |
| // | division (floor) | 
| % | modulus | 
| ** | exponent |

### :memo: To note: float division vs floor(integer) division
> 5 / 2 = 2.5  
> 5 // 2 = 2  
> 5 % 2 = 1  

## :three: Random python package
The python standard library has a package random.  To use it in your program you must import it.
```
import random
# program code goes below

```
You can take a look at the python docs here: [Random](https://docs.python.org/3/library/random.html)
Some functions available include:
- `randon.random()` Returns a floating point number between 0 and 1. 
- `random.randrange(stop)`  Returns an integer between 0 up until the value provided.  
- `random.randrange(start, stop, step)` Returns an integer from the range and step given.  
- `random.randint(a, b)`  Returns an integer between AND including a and b.  


---

# :floppy_disk: Dice Rolling


## Create a program that rolls a normal dice (6 sides)
The program then should be extended to roll any number of times, with the input being provided by the user.  
The output of each dice roll should be displayed.  

```
>>> Roll result: 3
>>> Roll again? (y/n):  y
>>> 
>>> Roll result: 5
>>> Roll again? (y/n): n
>>>
>>> K. Bye

```

## Create a new dice that prompts the user for how many sides on their dice.  
The program should then roll and print the result until it lands on the highest-sided number.  
```
>>> Enter the number of sides: 15
>>>
>>> 1 3 12 14 7 8 8 3 2 4 15 
>>>
>>> It took 11 rolls to get 15.  
```

```
>>> Enter the number of sides: 3
>>>
>>> 1 3
>>>
>>> It took 2 rolls to get 3.  
```

# :floppy_disk: Binary Conversion
The program should accept a positive whole number and output the corresponding value in binary.  

![Converting to Binary](https://media.geeksforgeeks.org/wp-content/uploads/decimal2binary.png)

*Note that converting to binary is essentially repeated division by 2 and using the quotient's remainder.  

```
>>> Please enter a postive whole number: 11  
>>> 11 in binary is: 1011
>>> 
```
