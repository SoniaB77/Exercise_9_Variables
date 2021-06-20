# Exercise 9 - Variables

Objectives: 

* To practice with variables and types
* To use the input function
* To become familiar with some built-in functions and methods

Tasks: 

Part 1: Practice declaring variables and using different types

1. Create a new PyCharm project: Exercise9.
2. Add a new Python file to the project called types.py
3. Within this file, create two variables: one containing your first name and another containing your last name.
4. Use the print function to output your full name with a space between your first and last name.
5. Now transfer these variable values into a list and display the list.
6. Take the variables and now store the values in a dictionary, using the keys 'first' and 'last'. Display the dictionary values.

Part 2: Practice with methods and functions

1. Create a new PyCharm file in the same project called operations.py.
2. Type the following code: var = input("Please enter a value: ")
This is an easy way of outputting a prompt to the console and getting a reply. The variable var is a reference to that reply, which is a string.
3. Now print the following:
a) The value of var as upper case.
b) The number of characters in var (this does not require a method).
c) Does it contain numeric characters? (try the isdecimal() method).

Part 3: Practice with complex maths

1. Create a new PyCharm file in the same project called projectile.py.

The height of a projectile (y) from a gun (ignoring air resistance) is given as:

`y = y0 + x tan theta - (gx^2) / (2(v0 cos θ)2)`

where:

g : Acceleration due to gravity: 9.81 m/s squared
v0 : the initial velocity m/s
θ : (theta) elevation angle in radians
x : the horizontal distance travelled
y0 : height of the barrel (m)

Write a Python program to answer the following question:

At a barrel height of 1m, after a horizontal distance of 0.5m, an elevation of 80 degrees, and an initial velocity of 44 m/s, what is the height of the projectile?
To convert degrees (deg) to radians use:
theta = deg * (pi/180)
You will need to import some math methods:
from math import pi, tan, cos