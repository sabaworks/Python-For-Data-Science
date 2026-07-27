"""
===================================================
Topic: String Methods in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
===================================================
"""


#==================================================
# Question 1: What are String Methods?
#==================================================
# String methods are built-in functions that are
# used to perform different operations on strings,
# such as changing case, searching, replacing,
# counting, splitting, and removing spaces.


#==================================================
# Question 2: Why do we use String Methods?
#==================================================
# We use string methods to:
# ✔ Convert text to uppercase or lowercase.
# ✔ Format text in different styles.
# ✔ Remove unwanted spaces.
# ✔ Replace words or characters.
# ✔ Search for characters or words.
# ✔ Count occurrences of characters.
# ✔ Split a string into a list.
# ✔ Check how a string starts or ends.
# ✔ Make string manipulation easier and faster.


#=================================================
#             Syntax
#=================================================
# string.method()

# Example:
# text = "python"
# print(text.upper())


#=================================================
# Task 1: Convert Text to Uppercase
#=================================================
text = "python"
print(text.upper())


#=================================================
# Task 2: Convert Text to Lowercase
#=================================================
text = "DATA SCIENCE"
print(text.lower())


#=================================================
# Task 3: Convert Text to Title Case
#=================================================
text = "welcome to python"
print(text.title())


#=================================================
# Task 4: Remove Leading and Trailing Spaces
#=================================================
text = " Hello World "
print(text.strip())


#=================================================
# Task 5: Replace a Word in a String
#=================================================
text = "I love C++"
print(text.replace("C++", "Python"))


#=================================================
# Task 6: Count the Occurrences of a Character
#=================================================
text = "banana"
print(text.count("a"))


#=================================================
# Task 7: Find the Position of a Character
#=================================================
course_name = "Machine Learning"
print(course_name.find("L"))

#===========================================================
# Task 8: Check if a String Starts with Specific Characters
#===========================================================
text = "python"
print(text.startswith("py"))


#==================================================
# Task 9: Split a String into a List
#==================================================
text = "Artificial Intelligence"
print(text.split())


#==================================================
# Task 10: Find the Length of a String
#==================================================
text = "Programming"
print(len(text))


#==================================================
# Task 11: Convert Text to Capitalized Form
#==================================================
text = "python programming"
print(text.capitalize())


#==================================================
# Task 12: Check if String Ends with "ing"
#==================================================
text = "Programming"
print(text.endswith("ing"))


#==================================================
# Task 13: Find the Index of "o"
#==================================================
text = "Hello World"
print(text.index("o"))


#==================================================
# Task 14: Check if String Contains Only Alphabets
#==================================================
text = "Python"
print(text.isalpha())


#==================================================
# Task 15: Check if String Contains Only Digits
#==================================================
text = "2026"
print(text.isdigit())


#==================================================
# Task 16: Check if String is Alphanumeric
#==================================================
text = "Python123"
print(text.isalnum())


#==================================================
# Task 17: Center a String
#==================================================
text = "Python"
print(text.center(20))


#==================================================
# Task 18: Swap Uppercase and Lowercase Letters
#==================================================
text = "PyThOn"
print(text.swapcase())


#==================================================
# Task 19: Join Words into a String
#==================================================
word_list = ["Python", "is", "Awesome"]
print(" ".join(word_list))


#==================================================
# Task 20: Check if All Characters are Lowercase
#==================================================
text = "python"
print(text.islower())


#==================================================
#                    Summary
#==================================================
# ✔ String methods are built-in functions.
# ✔ They perform different operations on strings.
# ✔ Methods do not change the original string unless reassigned.
# ✔ upper() converts text to uppercase.
# ✔ lower() converts text to lowercase.
# ✔ title() converts text to title case.
# ✔ strip() removes extra spaces.
# ✔ replace() replaces text.
# ✔ count() counts occurrences.
# ✔ find() returns the index of a character.
# ✔ startswith() and endswith() check prefixes and suffixes.
# ✔ split() converts a string into a list.
# ✔ len() returns the length of a string.
# ✔ String methods return a new string because strings are immutable.


#=================================================
# End of Topic
#=================================================
# ✔ Topic Completed Successfully.
# ✔ Next Topic: Lists
# Happy Coding! 🚀
