"""
=========================================
Topic: Tuples in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
=========================================
"""

# ========================================
# What is a Tuple?
# ========================================
# A tuple is an ordered collection of items.
# It can store different types of data, but
# its values cannot be changed after creation.


# ========================================
# Why Use Tuples?
# ========================================
# Tuples are used to store data that should
# not be modified. They are faster than lists
# and help protect important data from changes.


# ========================================
# Task 1 - Create a Tuple
# ========================================
colors = ("Red", "Blue", "Green")
print(colors)


# ========================================
# Task 2 - Indexing in Tuple
# ========================================
fruits = ("Apple", "Banana", "Mango", "Orange")
print(fruits[0])
print(fruits[-1])


# ========================================
# Task 3 - Negative Indexing 
# ========================================
numbers = (10, 20, 30, 40, 50)
print(numbers[-2])


# ========================================
# Task 4 - Slicing in Tuple
# ========================================
cities = ("Lahore", "Karachi", "Islamabad", "Multan", "Peshawar")
print(cities[0:3])
print(cities[3:5])


# ========================================
# Task 5 - Find Length
# ========================================
students = ("Ali", "Sara", "Ahmed", "Ayesha")
print(len(students))


# ========================================
# Task 6 -  Check Item Exists
# ========================================
languages = ("Python", "Java", "C++")
print("Python" in languages)


# ========================================
# Task 7 - count() Method
# ========================================
numbers = (10, 20, 10, 30, 10, 40)
count_10 = numbers.count(10)
print("Count of 10:", count_10)


# ========================================
# Task 8 - index() Method 
# ========================================
fruits = ("Apple", "Banana", "Mango", "Orange")
index_mango = fruits.index("Mango")
print("Index of Mango is:", index_mango)


# ========================================
# Task 9 -  Tuple Packing
# ========================================
student = "Saba", 19, "Data Science"
print(student)


# ========================================
# Task 10 - Tuple Unpacking
# ========================================
student = ("Saba", 19, "Data Science")
name, age, field = student
print("Name:", name)
print("Age:", age)
print("Field:", field)


# ========================================
# Task 11 - Single Element Tuple 
# ========================================
fruit = ("Apple",) # Note the comma after "Apple"
print(fruit)
print(type(fruit))


# ========================================
# Task 12 - Tuple vs List
# ========================================
languages = ["Python", "Java"]
subjects = ("Math", "Physics")

# Adding an item to the list
languages.append("C++")
print("Updated List:", languages)

# Tuples are immutable.
# The following line will raise an AttributeError.
# subjects.append("Chemistry")

# List:
# Items can be added, removed, and modified.

# Tuple:
# Items cannot be added, removed, or modified after creation.


# ========================================
# Summary
# ========================================
#  Create a Tuple
#  Access Tuple Items (Indexing)
#  Negative Indexing
#  Tuple Slicing
#  Find Tuple Length using len()
#  Check Item Exists using in Operator
#  count() Method
#  index() Method
#  Tuple Packing
#  Tuple Unpacking
#  Single Element Tuple
#  List vs Tuple
#  Immutable Tuples (Tuples cannot be modified)


# ========================================
# Topic Completed Successfully 
# Next Topic: Dictionaries
# Happy Coding! 🚀
# ========================================
