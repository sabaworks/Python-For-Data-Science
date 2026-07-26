"""
=========================================
Topic: String Formatting in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
=========================================
"""

#========================================
# Question 1: What is String Formatting?
#========================================
# String formatting is a technique used to insert
# variables or expressions into a string to create
# readable and dynamic output.


#=============================================
# Question 2: Why do we use String Formatting?
#=============================================
# We use string formatting to:
# ✔ Combine text and variables.
# ✔ Display values in a clean and readable way.
# ✔ Avoid writing multiple print statements.
# ✔ Make the code easier to understand.
# ✔ Reduce code repetition.


#=================================
#             Syntax
#=================================
# f"Text {variable}"

# Example:
# name = "Saba"
# print(f"My name is {name}")


#=================================================
# Task 1: Print Name and Age Using an f-string
#=================================================
name = "Saba"
age = 20
print(f"{name} is {age} years old.")


#=================================
# Task 2: Print City and Country
#=================================
city = "Lahore"
country = "Pakistan"
print(f"I live in {city}, {country}.")


#=======================================
# Task 3: Print the Sum of Two Numbers
#=======================================
num1 = 15
num2 = 25
print(f"The sum is {num1 + num2}.")


#=======================================
# Task 4: Print Course Information
#=======================================
course = "Python"
duration = 3
print(f"I'm learning {course} for {duration} months.")


#========================================
# Task 5: Print Student Information
#========================================
name = "Saba"
cgpa = 3.24
university = "BGNU"
print(f"{name} studies at {university} and has a CGPA of {cgpa}.")


#============================================
# Task 6: Use String Methods with f-strings
#============================================
name = "saba"
marks = 95
subject = "python"
print(f"{name.capitalize()} scored {marks} in {subject.capitalize()}.")


#=======================================
# Task 7: Print Multiplication Result
#=======================================
a = 12
b = 5
print(f"{a} × {b} = {a * b}")

#=======================================
# Task 8: Print Temperature
#=======================================
temperature = 32
print(f"Today's temperature is {temperature}°C.")


#========================================
# Task 9: Print Percentage
#========================================
percentage = 91.5
print(f"My percentage is {percentage}%.")


#========================================
# Task 10: Print Full Name
#========================================
first_name = "Saba"
last_name = "Ishaq"
print(f"My full name is {first_name} {last_name}.")


#==================================================
#                    Summary
#==================================================
# ✔ String formatting is used to insert variables into strings.
# ✔ f-strings provide a simple and readable way to format text.
# ✔ Variables are written inside curly braces {}.
# ✔ Expressions can also be used inside {}.
# ✔ String methods can be used with f-strings.
# ✔ String formatting makes the output cleaner and more professional.
# ✔ Expressions like addition and multiplication can be used inside {}.
# ✔ f-strings were introduced in Python 3.6.

#=====================================
# End of Topic
#=====================================
# ✔ Topic Completed Successfully.
# ✔ Next Topic: String Methods
# Happy Coding! 🚀