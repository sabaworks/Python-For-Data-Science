"""
===============================================
Topic: Functions in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
===============================================
""" 

#==========================================================
# What is a Function?
#==========================================================

# A function is a reusable block of code that performs
# a specific task. Instead of writing the same code
# multiple times, we write it once inside a function
# and call it whenever needed.


#==========================================================
# Why Do We Use Functions?
#==========================================================

# ✔ To avoid writing repetitive code.
# ✔ To make programs easier to read.
# ✔ To improve code reusability.
# ✔ To organize large programs into smaller parts.
# ✔ To make debugging and maintenance easier.


#==========================================================
# Basic Syntax
#==========================================================

# def function_name(parameters):
#     # Function Body
#     return value

# Calling a Function:
# function_name(arguments)


#==========================================================
# Task 1 : Create and Call a Simple Function
#==========================================================
def greet():
    print("Welcome to Python")
greet()
greet()


#==========================================================
# Task 2 : Print Student Information
#========================================================== 
def student_name():
    print("My name is Saba")
student_name()
student_name()
student_name()    


#==========================================================
# Task 3 : Function with One Parameter
#==========================================================
def greet(name):
    print("Hello", name)

greet("Ali")


#==========================================================
# Task 4 : Return the Square of a Number
#==========================================================
def square(num):
    return num * num
result = square(5)
print(result)


#==========================================================
# Task 5 : Add Two Numbers
#==========================================================
def add(a,b):
    return a + b
answer = add(15 , 25)
print(answer)


#==========================================================
# Task 6 : Default Function Parameter
#==========================================================
def country(name = "Pakistan"):
    print(name)
country()
country("Turkey")    


#==========================================================
# Task 7 : Default Argument Example
#==========================================================
def multiply(a, b = 2):
    return a * b
result1 = multiply(5)
result2 = multiply(5, 4)
print(result1)
print(result2)


#==========================================================
# Task 8 : Local vs Global Variable
#==========================================================
name = "Saba"      # Global Variable

def student():
    name = "Dev"   # Local Variable
    print(name)

student()
print(name)


#==========================================================
# Task 9 : Keyword Arguments
#==========================================================
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)
student_info(name = "Ali", age = 20)


#==========================================================
# Task 10 : Returning a Formatted String
#==========================================================
def info(name, city):
    return f"{name} lives in {city}"

message = info(city="Lahore", name="Ali")
print(message)


#==========================================================
# Task 11 : Variable-Length Arguments (*args)
#==========================================================
def add(*numbers):
    print(type(numbers))   # Output: <class 'tuple'>
    total = 0
    for num in numbers:
        total = total + num
    return total
result = add(10, 20, 30, 40)
print(result)

#==========================================================
# Task 12 : Keyword Variable-Length Arguments (**kwargs)
#==========================================================
def student_details(**data):
    for key, value in data.items():
      print(key, ":", value)
    print(data.get("name"))
    # get() safely accesses a value from **kwargs.

student_details(name="Ali", age=20, city="Lahore")


#==========================================================
# Task 13 : Multiply Using *args
#==========================================================
def multiply(*numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total
answer = multiply(2, 3, 4)
print(answer)    


#==========================================================
# Task 14 : Access Data Using **kwargs
#==========================================================
def student_profile(**info):
    return info.get("city")
city_name = student_profile(name="Ali", age=20, city="Lahore")
print(city_name)


#==========================================================
# Task 15 : Function with Decision Making
#==========================================================
def calculate(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
result = calculate(10, 20, 15, 30)
if result > 50:
    print("Pass")
else:
    print("Fail")    


#==========================================================
# Task 16 : Mixed Parameters (Normal + **kwargs)
#==========================================================
def person_details(name, **info):
    print(name)
    print(info)
    return info.get("city")

city_name = person_details(
    "Ali",
    age=20,
    city="Lahore",
    university="BGNU"
)
print(city_name)


#==========================================================
# Task 17 : Student Marks Report
#==========================================================
def student_marks(student , *marks):
    total = 0
    for mark in marks:
        total = total + mark
    return f"{student} scored {total} marks"
message = student_marks("Ali", 80, 90, 85)
print(message)    


#==========================================================
# Task 18 : Employee Details Report
#==========================================================
def employee_details(department, **details):
    print(department)
    print(details.get("name"))
    print(details.get("salary"))
    return details.get("salary")
salary = employee_details(
    "Data Science",
    name="Saba",
    age=20,
    salary=80000,
    city="Nankana Sahib"
)

print(salary)


#==========================================================
# Task 19 : Student Performance Report
#==========================================================
def student_report(name, *marks, **info):
    total = 0
    for mark in marks:
        total = total + mark
    print("Name:", name)
    print("Total Marks:", total)
    print("City:", info.get("city"))
    return info.get("age")
age = student_report(
    "Ali",
    80, 90, 85,
    city="Lahore",
    age=20
)

print(age)


#==========================================================
# Task 20 : Company Salary Report
#==========================================================
def company_salary(company, *salaries, **details):
    total = 0
    for salary in salaries:
        total = total + salary
    print("Company:", company)
    print("Total Salary:", total) 
    print("Manager:", details.get("manager"))
    return details.get("city")

city = company_salary(
    "TechSoft",
    50000, 60000, 70000,
    manager="Saba",
    city="Lahore"
)

print(city)


#==========================================================
# Summary
#==========================================================

# ✔ Functions help avoid repetitive code.
# ✔ Functions improve code readability.
# ✔ def is used to create a function.
# ✔ A function is executed by calling it.
# ✔ Parameters receive values from arguments.
# ✔ return sends a value back to the caller.
# ✔ Default parameters provide predefined values.
# ✔ Keyword arguments improve readability.
# ✔ *args accepts multiple positional arguments.
# ✔ **kwargs accepts multiple keyword arguments.
# ✔ Local variables exist only inside a function.
# ✔ Global variables can be accessed outside functions.
# ✔ Functions make programs modular and reusable.

#==========================================================
# End of Topic
#==========================================================

# You have successfully completed Functions in Python.
# Next Topic : Exception Handling
# Happy Coding!🚀
#==========================================================
