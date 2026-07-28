"""
===================================================
Topic: Lists in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
===================================================
"""

#==================================================
# Question 1: What is a List?
#==================================================

# A list is a built-in data type in Python used to
# store multiple items in a single variable.
# Lists are ordered, mutable, and allow duplicate values.


#==================================================
# Question 2: Why Do We Use Lists?
#==================================================

# We use lists to:
# ✔ Store multiple values in one variable.
# ✔ Access items using indexes.
# ✔ Add, remove, and modify items.
# ✔ Store different data types in one collection.
# ✔ Process data easily using loops.
# ✔ Keep related information organized.

#==================================================
# Syntax
#==================================================
# Lists are enclosed in square brackets [].
# list_name = [item1, item2, item3]

# Example

# fruits = ["Apple", "Banana", "Mango"]


#==================================================
# Task 1: Create a List
#==================================================
colors = ["Red","Blue","Green"]
print(colors)


#==================================================
# Task 2: Access List Items Using Indexing
#==================================================
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[0])  
print(fruits[-1])  


#==================================================
# Task 3: Access Items Using Negative Indexing
#==================================================
numbers = [10, 20, 30, 40, 50]
print(numbers[-2])


#==================================================
# Task 4: Slice a List
#==================================================
cities = ["Lahore", "Karachi", "Islamabad", "Multan", "Peshawar"]
print(cities[0:3])
print(cities[3:])


#==================================================
# Task 5: Modify a List Item
#==================================================
animals = ["Cat", "Dog", "Rabbit"]
animals[1] = "Lion"
print(animals)


#==================================================
# Task 6: Find the Length of a List
#==================================================
students = ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"]
print(len(students))


#==================================================
# Task 7: Check if an Item Exists
#==================================================
languages = ["Python", "Java", "C++"]
print("Python" in languages)


#==================================================
# Task 8: Iterate Through a List Using a Loop
#==================================================
flowers = ["Rose", "Tulip", "Lily"]
for flower in flowers:
    print(flower)


#===================================================
# Task 9: Store Different Data Types in a List
#===================================================
person = ["Saba", 20, 3.31, True]
print(person)


#====================================================
# Task 10: Reverse a List Using Slicing
#====================================================
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])


#====================================================
# Task 11: Add an Item Using append()
#====================================================
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)


#====================================================
# Task 12: Insert an Item Using insert()
#====================================================
colors = ["Red", "Blue", "Green"]
colors.insert(1, "Yellow")
print(colors)


#====================================================
# Task 13: Remove an Item Using remove()
#====================================================
animals = ["Cat", "Dog", "Rabbit", "Lion"]
animals.remove("Rabbit")
print(animals)


#====================================================
# Task 14: Remove an Item Using pop(Index)
#====================================================
numbers = [10, 20, 30, 40, 50]
removed_value = numbers.pop(2)
# print the removed value.
print("Removed value:", removed_value)
print("Updated list:", numbers)


#====================================================
# Task 15: Remove the Last Item Using pop()
#====================================================
letters = ["A", "B", "C", "D"]
removed_letter = letters.pop()
print("Removed letter:", removed_letter)    


#====================================================
# Task 16: Remove All Items Using clear()
#====================================================
students = ["Ali", "Sara", "Ahmed"]
students.clear()
print(students) 


#====================================================
# Task 17: Use Multiple List Methods
#====================================================
cars = ["BMW", "Audi"]
cars.append("Honda")
cars.insert(1, "Toyota") 
print(cars)


#====================================================
# Task 18: Remove and Add Items
#====================================================
languages = ["Python", "Java", "C++"]
languages.remove("Java")
languages.append("JavaScript")
print(languages)


#====================================================
# Task 19: Store the Removed Item
#====================================================
fruits = ["Apple", "Banana", "Mango"]
removed_fruit = fruits.pop(1)
print("Removed fruit:", removed_fruit)


#====================================================
# Task 20: Practice List Operations
#====================================================
data = [10, 20, 30]
data.append(40)
data.insert(1, 15)
data.remove(30)
data.pop(-1) 
print(data)


#====================================================
# Task 21: Find the Index of an Item
#====================================================
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.index("Mango")
print(fruits.index("Mango"))  


#====================================================
# Task 22: Count the Occurrences of an Item
#====================================================
numbers = [10, 20, 10, 30, 10, 40]
count = numbers.count(10)
print(count)


#====================================================
# Task 23: Sort a List
#====================================================
numbers = [50, 20, 10, 40, 30]
numbers.sort()
print(numbers)


#====================================================
# Task 24: Reverse a List
#====================================================
letters = ["A", "B", "C", "D"]
letters.reverse()
print(letters)


#===================================================
# Task 25: Create a Copy of a List
#===================================================
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)


#===================================================
# Task 26: Count and Find Items
#===================================================
names = ["Ali", "Sara", "Ahmed", "Sara", "Bilal"]
count_sara = names.count("Sara")
index_Ahmed = names.index("Ahmed")
print("Count of Sara:", count_sara)
print("Index of Ahmed:", index_Ahmed)


#===================================================
# Task 27: Sort Strings Alphabetically
#===================================================
fruits = ["Mango", "Apple", "Banana", "Orange"]
alphabetical_sort = sorted(fruits)
print(alphabetical_sort)


#===================================================
# Task 28: Reverse Numbers in a List
#===================================================
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)


#===================================================
# Task 29: Copy and Modify a List
#===================================================
list1 = ["Python", "Java"]
list2 = list1.copy()
list2.append("C++")
print("Original list:", list1)
print("Modified list:", list2)


#===================================================
# Task 30: Challenge – Multiple List Operations
#===================================================
data = [5, 2, 9, 2, 7]
count_2 = data.count(2)
index_9 = data.index(9)
sortingdata = sorted(data)
sortingdata.reverse()
print("Count of 2:", count_2)
print("Index of 9:", index_9)
print("Sorted data:", sortingdata)
print("Reverse sorted data:", sortingdata)


#===================================================
# Bonus Task: Understand copy() Method
#===================================================
numbers = [10, 20, 30]
new_list = numbers.copy()
new_list.append(40)
print(numbers)
print(new_list)


#===================================================
# Summary
#===================================================

# ✔ A list stores multiple items in one variable.
# ✔ Lists are ordered and mutable.
# ✔ Duplicate values are allowed.
# ✔ Items are accessed using indexes.
# ✔ Negative indexing accesses items from the end.
# ✔ Slicing extracts a portion of a list.
# ✔ append() adds an item to the end.
# ✔ insert() adds an item at a specific position.
# ✔ remove() deletes an item by value.
# ✔ pop() removes an item by index or the last item.
# ✔ clear() removes all items.
# ✔ index() finds the position of an item.
# ✔ count() counts occurrences of an item.
# ✔ sort() sorts the list.
# ✔ reverse() reverses the list.
# ✔ copy() creates a separate copy of a list.
# ✔ Lists support indexing and slicing.


#===================================================
# End of Topic
#===================================================

# ✔ Topic Completed Successfully.
# ✔ Next Topic: Tuples
# Happy Coding! 🚀