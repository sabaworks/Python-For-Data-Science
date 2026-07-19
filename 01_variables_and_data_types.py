"""
==========================================
Topic: Variables and Data Types

Course:
IBM Python for Data Science, AI & Development

Concepts Covered:
- Variables
- Integer
- Float
- String
- Boolean
- type()
- Variable Reassignment
- Input Function

Author: Saba
==========================================
"""
# ========================================
# What are Variables?
# ========================================
# A variable is a named container used to store data.
# The value stored in a variable can be changed during
# program execution.

# ========================================
# What are Data Types?
# ========================================
# Data types define what kind of value a variable stores.
# Common data types include int, float, str, and bool.

# ========================================
# Examples
# ========================================



# ========================================
# Task 1 - Basic Integer
# ========================================
age = 18
print("My age is ", age)


# ========================================
# Task 2 - String Variable
# ========================================
name = "Saba"
print(name) 

# ========================================
# Task 3 - Boolean Data Type
# ========================================
is_student = True
print(type(is_student))


# ========================================
# Task 4 - Multiple Variables
# ========================================
city = "Lahore"
country = "Pakistan"
marks = 900
print(city)
print(country)
print(marks)


# ========================================
# Task 5 - Check Data Types
# ========================================
a = 10
b = "Dev"
c = 3.13
d = False
print("Type of a is", type(a))
print("Type of b is", type(b))
print("Type of c is", type(c))
print("Type of d is", type(d))


# ========================================
# Task 6 - Variable Reassignment
# ========================================
score = 50
score = 80
print(score) 
# The new value replaces the previous value.
# Final value stored in 'score' is 80.


# ========================================
# Task 7 - Float Type
# ========================================
price = 99.90
print(price)


# ========================================
# Task 8 Mixed Output
# ========================================
name = "Saba Dev"
age = 18
cgpa = 3.13
print(name, age, cgpa)


# ========================================
# Task 9 - Change Variable Type
# ========================================
x = 10
print(type(x))
x = "Ten"
print(type(x))


# ========================================
# Task 10 - Mini Challenge 
# ========================================
name = "Saba Rajput"
age = 18
height = 5.2
is_programmer = True
print("Name: ", name)
print("Age: ", age )
print("Height: ", height)
print("Programmer: ", is_programmer) 


# ========================================
# Task 11 - Bonus Challenge ( Input )
# ========================================
name = input("Enter your name: ")
print("Hello,", name)


# ========================================
# Summary
# ========================================
# ✔ Variables
# ✔ Data Types
# ✔ type()
# ✔ Variable Reassignment
# ✔ Input Function


# ========================================
# End of Topic
# Next Topic: Type Casting
# ========================================