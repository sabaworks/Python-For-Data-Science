"""
=========================================
Topic: Type Casting in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
=========================================
""" 


# ========================================
# What is Type Casting?
# ========================================
# Type Casting is the process of converting
# one data type into another data type.


# ========================================
# Why Use Type Casting?
# ========================================
# Type Casting helps us convert data into
# the required type so that we can perform
# calculations and other operations correctly.


#===========================
#         EXAMPLES
#===========================


# ========================================
# Example 1 - String Concatenation
# ========================================
first_number = "9"
second_number = "8"
print(first_number + second_number)

# Output: 98
# Both values are strings, so the + operator
# concatenates them instead of adding them.


# ========================================
# Example 2 - Integer Addition
# ========================================
first_number = 9
second_number = 8
print(first_number + second_number)

# Output: 17
# Integers are added mathematically.


# ===========================================
# Example 3 - String Concatenation with Names
# ===========================================
first_name = "Saba"
last_name = "Ishaq"
print(first_name + " " + last_name)

# Output: Saba Ishaq


# ============================================
# Example 4 - Explicit Type Casting using int()
# ============================================
first_number = "9"
second_number = "8"
result = int(first_number) + int(second_number)
print(result)

# Output: 17
# Strings are converted into integers before addition.


# ========================================
# Example 5 - Implicit Type Casting
# ========================================
integer_number = 5
float_number = 2.0
result = integer_number + float_number
print(result)

# Output: 7.0
# Python automatically converts the integer
# into a float before performing the addition.


# ========================================
# Example 6 - Explicit Type Casting
# ========================================
integer_number = 5
float_number = 2.0
result = float(integer_number) + float_number
print(result)

# Output: 7.0
# We explicitly convert the integer into
# a float using the float() function.


#===========================
#         TASKS
#===========================


# ========================================
# Task 1 - Convert Float to Integer
# ========================================
price = 99.99
integer_price = int(price)
print(integer_price)


# ============================================
# Task 2 - User Input and Integer Conversion
# ============================================
age = input("Enter your age: ")
age = int(age)
print(age)
print(type(age))
 

# =============================================
# Task 3 - Convert String to Float and Integer
# =============================================
number = "25"
integer_number = int(number)
float_number = float(number)
print(integer_number)
print(float_number)


# =============================================
# Task 4 - Division Result as Float and Integer
# =============================================
a = 15
b = 4
print(float(a/b))
print(int(a/b))


# ========================================
# Task 5 - Convert String to Boolean
# ========================================
text = "True"
boolean_value = bool(text)
print(boolean_value)


# ========================================
# Task 6 - Convert Integer to String
# ========================================
marks = 95
marks = str(marks)
print(marks)
print(type(marks))


# ========================================
# Task 7 - Sum of Two User Inputs
# ========================================
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
total = int(first_number) + int(second_number)
print("Total:", total)


# ========================================
# Task 8 - Observe Decimal Removal
# ========================================
decimal_number = 7.999
print(int(decimal_number))


# ============================================
# Task 9 - Convert String to Float and Integer
# ============================================
price = "49.95"

float_price = float(price)
integer_price = int(float_price)

print(float_price)
print(integer_price)


# ========================================
# Task 10 - Type Casting Mini Challenge
# ========================================
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Type Casting to Integer
print(int(num1))
print(int(num2))

# Addition
print(int(num1) + int(num2))

# Subtraction
print(int(num1) - int(num2))

# Multiplication
print(int(num1) * int(num2))

# Division
print(int(num1) / int(num2))


# ========================================
# Bonus Task - Boolean Type Casting
# ========================================
zero_value = bool(0)
one_value = bool(1)
empty_string = bool("")
text_value = bool("Hello")

print(zero_value)
print(one_value)
print(empty_string)
print(text_value)


# ========================================
# Summary
# ========================================

# ✔ What is Type Casting?
# ✔ Why Use Type Casting?
# ✔ Implicit Type Casting
# ✔ Explicit Type Casting
# ✔ int() Function
# ✔ float() Function
# ✔ str() Function
# ✔ bool() Function
# ✔ User Input with Type Casting
# ✔ Type Casting Practice

# ========================================
# End of Topic
# Next Topic: Strings
# ========================================


