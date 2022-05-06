# -*- coding: utf-8 -*-
"""
Created on Thu May  5 20:20:32 2022
@author: Krishna Aryal
"""

# Data Types

# i. boolean -Store only two values (True or False)
# Example-1
# var1 = True # False
# print(var1)

# Example-2
# Accept boolean input from user (i.e. keyboard)
# declare variables
# var1 = None
# var2 = None

# input
# var1 = input("Enter any boolean value : ") # string input

# processing
# var2 = bool(var1) # type conversion (string to boolean)

# output
# print(var2)

# ii. Integer (whole number)
# Example-3
"""
num1 = 1
print(num1) # 1
num1 = num1 + 5
print(num1) # 6
"""

# Example-4
# Read integer value from keyboard
"""
var1 = None # decalre
var1 = input("Enter integer value : ") # input
var1 = int(var1) # process
var1 = var1 + 5
print(var1) # output
"""

# iii. float (decimal number/fractional number)
# Example-5
"""
var1 = 123.456
var1 = var1 + 78
print(var1)
"""

# Example-6
# Read floating point number from user
"""
var1 = None
var1 = input("Enter any float number : ") # string
var1 = float(var1) # string->float
var1 = var1 + 7
print(var1)
"""

# iv. String (Collection of characters)
# Example-7
# var1 = 'Broadway'
# var2 = "InfoSys"
# var3 = """Nepal"""
# print(var1, var2, var3)

# Example-8
# Read string from user
"""
var1 = None
var1 = input("Enter any string ") # input-> string
print(var1)
"""

# bool (Boolean), int (Integer), float (Floating Point), str (String) - basic types
# Reading value from keyboard - str
    # +, -, *, / - Cannt apply on str
    # str to int and apply +, -, *, /
    
# Type Conversion
    # Type Casting
        # Numeric to Numeric
    # Type Conversion
        # Numeric to String
        # String to Numeric

# Type Casting
# int to float
num1 = 15  # int
num2 = float(num1) # int -> float
print(num1)
print(num2)

# float to int
num3 = 123456.789   # float
num4 = int(num3)    # int  
print(num3)
print(num4)

# str to int
str1 = "123"
num5 = int(str1)
print(str1) # str
print(num5) # int

# int to str
num5 = 67
str1 = str(num5)
print(num5)
print(str1)


# str to float
str2 = "123.456"
num6 = float(str2)
print(str2)
print(num6)

# float to str
num6 = 456.321
str1 = str(num6)
print(str1)
print(num6)


# num7 = int("Hello")
# ValueError: invalid literal for int() with base 10: 'Hello'

# Explore varaible
import sys
var1 = 12345678910;
print(var1) # value of var1
print(type(var1))# value type - bool
print(id(var1)) # memory reference of variable
print(isinstance(var1, bool))
print(isinstance(var1, int)) # 0-False|1-True
print(isinstance(var1, float))
print(isinstance(var1, str))
print(sys.getsizeof(var1))

# Task1
    # Display the value of specific memory space. (1727995907760)
    # Display all the variables declare in memory. 






