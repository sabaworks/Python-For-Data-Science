"""
=========================================
Topic: Dictionaries in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
=========================================
"""


#========================================
# Question 1: What is a Dictionary?
#========================================

# A dictionary is a built-in data type in Python
# that stores data in the form of key-value pairs.
# Each key in a dictionary must be unique.


#===========================================
# Question 2: Why do we use Dictionaries?
#===========================================

# We use dictionaries to:
# ✔ Store data in key-value pairs.
# ✔ Access values using keys.
# ✔ Update existing values.
# ✔ Add or remove data easily.
# ✔ Organize related information.
# ✔ Search data quickly using keys.


#=================================
#             Syntax
#=================================

# dictionary_name = {
#     "key1": value1,
#     "key2": value2
# }


#==================================================
# Task 1: Access a Value Using a Key
#==================================================
student = {
    "name": "Saba",
    "age": 20,
    "city": "Lahore"
}

print(student["city"])


#==================================================
# Task 2: Update an Existing Value
#==================================================
student = {
    "name": "Saba",
    "age": 20
}
student["age"] = student["age"] + 5
print(student)


#==================================================
# Task 3: Access a Value Using get()
#==================================================
student = {
    "name": "Saba",
    "age": 20
}
print(student.get("city", "Not Available"))
print(student)


#==================================================
# Task 4: Update the Price in a Shopping Cart
#==================================================
cart = {
    "Laptop": 85000,
    "Mouse": 1200,
    "Keyboard": 3500
}
cart["Mouse"] = cart["Mouse"] + 300
print(cart)


#==================================================
# Task 5: Remove an Item Using pop()
#================================================== 
movies = {
    "Vincenzo": 9.2,
    "Bloodhounds": 8.8,
    "Big_Mouth": 9.1
}
removed = movies.pop("Bloodhounds")
print(removed)
print(movies)


#==================================================
# Task 6: Update Multiple Values Using update()
#==================================================
employee = {
    "name": "Ayesha",
    "department": "Data Science",
    "salary": 80000
}
employee.update({"salary": 85000, "city": "Lahore"})

print(employee)


#==================================================
# Task 7: Remove a Key and Display Its Value
#==================================================
account = {
    "name": "Ahmed",
    "balance": 15000,
    "account_type": "Savings"
}
amount = account.pop("balance")
print(amount)
print(account)


#==================================================
# Task 8: Update Data and Access a Missing Key
#==================================================
library = {
    "book": "Python Basics",
    "author": "John",
    "copies": 5
}
library["copies"] = library["copies"] - 2
x = library.get("publisher", "Unknown")
print(x)
print(library)


#==================================================
# Task 9: Delete and Add Dictionary Items
#==================================================
playlist = {
    "song1": "Believer",
    "song2": "Legends Never Die",
    "song3": "Shape of You"
}

del playlist["song2"]

playlist["song4"] = "Faded"

print(playlist)


#==================================================
# Task 10: Clear a Dictionary and Add New Data
#==================================================
scores = {
    "Ali": 95,
    "Sara": 88,
    "Ahmed": 91
}

scores.clear()

scores["Zara"] = 99

print(scores)


#==================================================
# Task 11: Create a Copy of a Dictionary
#==================================================
record = {
    "student": "Saba",
    "cgpa": 3.24
}

backup = record.copy()

backup["cgpa"] = 3.80

print(record)
print(backup)


#==================================================
# Task 12: Update, Remove, and Add Dictionary Items
#==================================================
profile = {
    "name": "Saba",
    "skills": "Python"
}

profile.update({"skills": "Python + SQL"})

x = profile.pop("name")

profile["city"] = "Nankana Sahib"

print(x)
print(profile)


#====================================================
# Task 13: Iterate Through a Dictionary Using items()
#====================================================
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}

for key, value in car.items():
    print(key, ":", value)


#==================================================
# Task 14: Modify and Retrieve Dictionary Values
#==================================================
employee = {
    "id": 101,
    "name": "Ayesha",
    "salary": 70000
}

employee["salary"] += 5000

del employee["id"]

print(employee.get("id", "Not Found"))
print(employee)


#===================================================
# Task 15: Copy, Update, and Remove Dictionary Items
#===================================================
inventory = {
    "Pen": 10,
    "Notebook": 5
}

backup = inventory.copy()

backup.update({"Pen": 15, "Pencil": 20})

removed = backup.pop("Notebook")

print(removed)
print(inventory)
print(backup)


#==================================================
# Task 16: Print Only Dictionary Keys
#==================================================
student = {
    "name": "Saba",
    "age": 20,
    "city": "Lahore"
}

for key in student.keys():
    print(key)


#==================================================
# Task 17: Print Only Dictionary Values
#==================================================
student = {
    "name": "Saba",
    "age": 20,
    "city": "Lahore"
}

for value in student.values():
    print(value)


#==================================================
# Task 18: Count Total Items in a Dictionary
#==================================================
student = {
    "name": "Saba",
    "age": 20,
    "city": "Lahore"
}

print(len(student))


#==================================================
# Task 19: Check if a Key Exists
#==================================================
student = {
    "name": "Saba",
    "age": 20
}

if "name" in student:
    print("Key Found")
else:
    print("Key Not Found")


#===================================================
# Task 20: Calculate the Total Value of All Products
#===================================================
products = {
    "Laptop": 85000,
    "Mouse": 1200,
    "Keyboard": 3500
}

total = 0

for price in products.values():
    total += price

print("Total Price:", total)


#==================================================
#                    Summary
#==================================================

# ✔ A dictionary stores data in key-value pairs.
# ✔ Keys must be unique.
# ✔ Values can be of any data type.
# ✔ Access values using keys or get().
# ✔ Update values using update() or assignment.
# ✔ Add new items by assigning a new key.
# ✔ Remove items using pop(), del, or clear().
# ✔ copy() creates a separate dictionary.
# ✔ items(), keys(), and values() are useful for looping.
# ✔ Dictionaries are mutable, so their data can be changed.


#=====================================
# End of Topic
#=====================================

# ✔ Topic Completed Successfully.
# ✔ Next Topic: Sets
# Happy Coding! 🚀