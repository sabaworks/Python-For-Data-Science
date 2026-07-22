"""
=========================================
Topic: Strings in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
=========================================
""" 

# ==================================================
# Question 1: What is a String?
# ==================================================
# A string is a sequence of characters used to store and represent text in Python.
# A string can contain letters, numbers, symbols, and spaces. Strings are written inside
# single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).


# ==================================================
# Question 2: Why Do We Use Strings?
# ==================================================
# Strings are used to store and work with text data. They help us display messages,
# take user input, manipulate text, search characters, and format output.

# Examples of using strings:
# • Storing a person's name
# • Displaying welcome messages
# • Taking input from the user


# ==================================================
# Task 1: Access Characters Using Indexing
# ==================================================
name = "DataScience"
print(name[0])  # Accessing the first character
print(name[10])  # Accessing the last character
print(name[4])  # Accessing the fifth character


# ==================================================
# Task 2: Print Each Character Using a For Loop
# ==================================================
st = input("Enter a string: ")
for char in st:
    print(char)


# ==================================================
# Task 3: Find the Length of a String
# ==================================================
st = "Python Programming" 
print(len(st))


# ==================================================
# Task 4: Print All Vowels from a String
# ==================================================
st = "Artificial Intelligence"
vowels = "aeiouAEIOU"
for char in st: 
    if char in vowels:
        print(char)


# ==================================================
# Task 5: Concatenate Two Strings
# ================================================== 
first = "Hello"
second = "World"
print(first + " " + second)


# ==================================================
# Task 6: Check Whether a String Starts with a Vowel
# ==================================================
name = input("Enter a name: ")
if name:
    vowels = "aeiouAEIOU"

    if name[0] in vowels:
        print("Starts with a vowel")
    else:
        print("Starts with a consonant")
else:
    print("Name cannot be empty.")


# ==================================================
# Task 7: Reverse a String Using Slicing
# ==================================================
def reverse(string):
    return string[::-1]
st = "MachineLearning"
print(reverse(st))


# ==================================================
# Task 8: Print Index and Character of a String
# ==================================================
text = "Python"
for i in range(len(text)):
    print(i, text[i])


# ==================================================
# Task 9: Display Information Using Strings
# ==================================================
name = "Ali"
field = "Data Science"
uni = "NUST"
print("My name is", name)
print("I study", field)
print("I study in", uni)


# ==================================================
# Task 10: Count Spaces in a String
# ==================================================
sen =  " I will be a great Data Scientist"
count = 0
for char in sen:
     if char == " ":
          count += 1
print("Spaces:" , count)         


# ==================================================
# Summary
# ==================================================
# What is a String?
# Why Do We Use Strings?
# Access Characters Using Indexing
# Print Each Character Using a For Loop
# Find the Length of a String
# Print All Vowels from a String
# Concatenate Two Strings
# Check Whether a String Starts with a Vowel
# Reverse a String Using Slicing
# Print Index and Character of a String
# Display Information Using Strings
# Count Spaces in a String


# ========================================
# End of Topic
# Next Topic: String Slicing
# Happy Coding! 🚀
# ========================================
