"""
===============================================
Topic: Sets in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
===============================================
""" 

#========================================
#          What are Sets?
#========================================

# A set is a built-in data type in Python
# that stores unique and unordered elements.
# Duplicate values are automatically removed.


#========================================
#         Why do we use Sets?
#========================================

# We use sets to:
# ✔ Store only unique values.
# ✔ Remove duplicate elements.
# ✔ Perform mathematical set operations.
# ✔ Check membership efficiently.
# ✔ Compare collections of data.


#=================================
#             Syntax
#=================================

# set_name = {value1, value2, value3}

# Example:

# languages = {"Python", "Java", "C++"}


#==================================================
# Task 1: Create a Set and Remove Duplicate Values
#==================================================
A = {10, 20, 20, 30, 10}

print(A)
# Duplicate values are automatically removed in a set.
print(len(A)) 

#==================================================
# Task 2: Add Elements to a Set
#==================================================
A = {1, 2, 3}
A.add(4)
A.add(2)

print(A)


#==================================================
# Task 3: Add Multiple Elements Using update()
#==================================================
A = {"Python", "Java"}
A.update(["C++", "Python", "SQL"])

print(A)


#=====================================================
# Task 4: Remove Elements Using remove() and discard()
#=====================================================
A = {10, 20, 30, 40}

A.remove(20)
A.discard(50)

print(A)


#==================================================
# Task 5: Perform Set Operations
#==================================================
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)


#==================================================
# Task 6: Check Subset, Superset, and Disjoint Sets
#==================================================
A = {1, 2, 3, 4}
B = {2, 3}

print(B.issubset(A))
print(A.issuperset(B))
print(A.isdisjoint(B))


#==================================================
# Task 7: Remove Duplicates from a List Using a Set
#==================================================
numbers = [10, 20, 20, 30, 40, 40]

unique_numbers = set(numbers)

unique_numbers.add(50)

unique_numbers.remove(20)

print(unique_numbers)
print(len(unique_numbers))


#==================================================
# Task 8: Find Common and Unique Elements
#==================================================
A = {"Ali", "Sara", "Ahmed"}
B = {"Sara", "Usman"}

C = A.intersection(B)
D = A.symmetric_difference(B)

print(C)
print(D)
print(len(D))


#==================================================
# Task 9: Convert a Tuple into a Set
#==================================================
data = ("Python", "Java", "Python", "C++")

languages = set(data)

languages.update(["SQL", "Java"])

languages.discard("C++")

print(languages)
print("Python" in languages)
print("HTML" not in languages)


#==================================================
# Task 10: Perform Multiple Set Operations
#==================================================
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

C = A - B
D = A ^ B
E = C.union({8})

print(C)
print(D)
print(E)
print(E.issubset(D))


#==================================================
# Task 11: Check if an Element Exists in a Set
#==================================================
fruits = {"Apple", "Banana", "Mango"}

print("Apple" in fruits)
print("Orange" in fruits)
print("Banana" not in fruits)


#==================================================
# Task 12: Remove All Elements from a Set
#==================================================
numbers = {10, 20, 30}

numbers.clear()

print(numbers)


#==================================================
# Task 13: Create a Copy of a Set
#==================================================
A = {1, 2, 3}

B = A.copy()

B.add(4)

print(A)
print(B)


#==================================================
# Task 14: Iterate Through a Set Using a Loop
#==================================================
colors = {"Red", "Green", "Blue"}

for color in colors:
    print(color)


#==================================================
# Task 15: Find the Number of Elements in a Set
#==================================================
skills = {"Python", "SQL", "Power BI", "Excel"}

count = 0

for skill in skills:
    count += 1

print(count)


#==================================================
#                    Summary
#==================================================

# ✔ A set stores unique and unordered elements.
# ✔ Duplicate values are removed automatically.
# ✔ Sets are mutable, but their elements must be immutable.
# ✔ add() adds a single element.
# ✔ update() adds multiple elements.
# ✔ remove() deletes an element and raises an error if it does not exist.
# ✔ discard() deletes an element without raising an error.
# ✔ Union combines two sets.
# ✔ Intersection returns common elements.
# ✔ Difference returns elements present in only one set.
# ✔ Symmetric difference returns uncommon elements.
# ✔ Sets are useful for removing duplicates and performing set operations.
# ✔ Sets do not support indexing because they are unordered.
# ✔ {} creates an empty dictionary.
# ✔ set() creates an empty set.


#=====================================
# End of Topic
#=====================================

# ✔ Topic Completed Successfully.
# ✔ Next Topic: Conditional Statements (if, elif, else)
# Happy Coding! 🚀