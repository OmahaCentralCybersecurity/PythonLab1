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
- Int to a string

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


# Dice Rolling

## Create a program that rolls a normal dice (6 sides)
The program then should be extended to roll any number of times, with the input being provided by the user.  
The output of each dice roll should be displayed.  
```
>>> Please enter the number of times you want to roll: 4
>>> Roll results: 3 3 2 6
>>> Roll again? (y/n):  y
>>> 
>>> Please enter the number of times you want to roll: 1
>>> Roll results: 5
>>> Roll again? (y/n): n
>>>

```

## Create a new dice that prompts the user for how many sides on their dice.  
The program should then roll 
