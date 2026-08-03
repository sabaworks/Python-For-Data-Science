"""
===============================================
Topic: Loops in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
===============================================
""" 


# ==========================================================
# WHAT IS A LOOP?
# ==========================================================
"""
A loop is a programming structure that executes a block of code
repeatedly until a condition becomes False or until all items
in a sequence are processed.
"""


# ==========================================================
# WHY DO WE USE LOOPS?
# ==========================================================
"""
1. To avoid writing the same code again and again.
2. To repeat a task automatically.
3. To process lists, tuples, strings, and other collections.
4. To make code shorter, cleaner, and more efficient.
"""

# ==========================================================
# TYPES OF LOOPS IN PYTHON
# ==========================================================

# 1. for Loop
# 2. while Loop


# ==========================================================
# FOR LOOP
# ==========================================================
"""
A for loop is used when the number of iterations is known
or when we want to iterate through a sequence such as a list,
tuple, string, or range.
"""

# Syntax
# for variable in sequence:
#     statement

# ==========================================================
# BREAK STATEMENT
# ==========================================================
"""-
The break statement immediately terminates the loop when
a specific condition becomes True.
"""

# ==========================================================
# CONTINUE STATEMENT
# ==========================================================
"""
The continue statement skips the current iteration and
moves to the next iteration of the loop.
"""

# ==========================================================
# Task 1 - Print Numbers from 1 to 5
# ==========================================================
for x in range(1,6):
    print(x)


# ==========================================================
# Task 2 - Countdown Using range()
# ==========================================================
for a in range(10, 0, -1):
    print(a)


# ==========================================================
# Task 3 - Iterate Through a List
# ==========================================================
fruits = ["Apple", "Banana", "Orange", "Mango"]
for fruit in fruits:
    print(fruit)


# ==========================================================
# Task 4 - Print Even Numbers
# ==========================================================
numbers = [4, 7, 10, 15, 18, 21]
for number in numbers:
    if number % 2 == 0:
        print(number)


# ==========================================================
# Task 5 - Calculate Total Marks
# ==========================================================
marks = [80, 75, 90, 85]
total = 0
for mark in marks:
    total = total + mark
print(total)


# ==========================================================
# Task 6 - Count Odd Numbers
# ==========================================================
numbers = [5, 8, 3, 10, 2, 7]
count = 0
for number in numbers:
    if number % 2 != 0:
        count = count + 1
print(count)


# ==========================================================
# Task 7 - break Statement Example
# ==========================================================
numbers = [12, 15, 18, 3, 20, 25]
for number in numbers:
    if number < 10:
        break
    print(number)


# ==========================================================
# Task 8 - continue Statement Example
# ==========================================================
numbers = [2, 5, 8, 9, 12, 15]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)


# ==========================================================
# Task 9 - Print Names with 5 or More Characters
# ==========================================================
names = ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"]
for name in names:
    if len(name) >= 5:  
        print(name)      


# ==========================================================
# Task 10 - break and continue Together
# ==========================================================
numbers = [5, 8, 12, 3, 20, 25, 2, 30]
for number in numbers:
    if number % 2 == 0:
        continue
    if number == 3:
        break
    print(number)


# ==========================================================
# WHILE LOOP
# ==========================================================

"""
A while loop repeats a block of code as long as the condition
remains True.
"""
# Syntax
# while condition:
#     statement


# ==========================================================
# Task 11 - Print Numbers Using while Loop
# ==========================================================
x = 1
while x < 6:
    print(x)
    x += 1


# ==========================================================
# Task 12 - Print Numbers Using while Loop
# ==========================================================
i = 5
while i < 10:
    print(i)
    i +=1


# ==========================================================
# Task 13 - Print Even Numbers Using while Loop
# ==========================================================
a = 2
while a <11:
    print(a)
    a += 2


# ==========================================================
# Task 14 - Print Odd Numbers Using while Loop
# ==========================================================
y = 1
while y <10:
    print(y)
    y += 2 


# ==========================================================
# Task 15 - Iterate Through a List Using while Loop
# ==========================================================
fruits = ["Apple", "Banana", "Orange", "Mango"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# ==========================================================
# Task 16 - break in while Loop
# ==========================================================
numbers = [8, 12, 15, 3, 20, 25]
i = 0
while i < len(numbers):
    if numbers[i] < 10:
        break
    print(numbers[i])
    i += 1


# ==========================================================
# Task 17 - continue in while Loop
# ========================================================== 
numbers = [2, 5, 8, 9, 12, 15]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        i += 1
        continue
    print(numbers[i])
    i += 1
    

# ==========================================================
# Task 18 - Sum of Numbers Using while Loop
# ==========================================================
numbers = [10, 20, 30, 40, 50]
i = 0
total = 0
while i < len(numbers):
        total = total + numbers[i]
        i += 1
print(total)

    
# ==========================================================
# Task 19 - Calculate Total Marks Using while Loop
# ==========================================================
marks = [80, 75, 90, 85]
i = 0
total = 0
while i < len(marks):
    total = total + marks[i]
    i += 1
print(total)    
    

# ==========================================================
# Task 20 - Count Even Numbers Using while Loop
# ==========================================================
numbers = [5, 8, 3, 10, 2, 7]
i = 0
count = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        count = count + 1
    i += 1
print(count)


# ==========================================================
# Summary
# ==========================================================

# ✔ What is a Loop?
# ✔ Why Use Loops?
# ✔ Types of Loops
# ✔ for Loop
# ✔ while Loop
# ✔ range() Function
# ✔ Looping Through Lists
# ✔ Counting Values
# ✔ Finding Sum Using Loops
# ✔ Even and Odd Number Examples
# ✔ Loop Control Statements (break and continue)

# ==========================================================
# Topic Completed Successfully
# Next Topic: Functions
# Happy Coding! 🚀
# ==========================================================

