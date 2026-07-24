"""
=========================================
Topic: String Slicing in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
=========================================
""" 

#========================================
# Question 1: What is String Slicing?
#========================================
# String slicing is a technique used to access or extract
# a specific part of a string using indexes.


#===========================================
# Question 2: Why do we use String Slicing?
#===========================================
# We use string slicing to extract characters, words, reverse
# strings, skip characters, and manipulate text easily.

#=================================
#             Syntax
#=================================
# string[start : stop : step]
# start -> Starting index (included)
# stop  -> Ending index (excluded)
# step  -> Number of positions to move


#=============================================
# Task 1: Print "Data" from "DataScience"
#=============================================
text = "DataScience"
print(text[0:4])


#=================================================
# Task 2: Print "Learning" from "MachineLearning"
#=================================================
text = "MachineLearning"
print(text[7:])


#==========================================
# Task 3: Print the Last 5 Characters
#==========================================
text = "Artificial"
print(text[-5:]) 


#===============================
# Task 4: Reverse a String
#===============================
text = "Pakistan"
print(text[::-1])


#=======================================
# Task 5: Print Every Second Character
#=======================================
text = "Computer"
print(text[::2])


#========================================
# Task 6: Print First and Last Character
#========================================
text = "University"
print(text[0])
print(text[-1:])

#======================================================
# Task 7: Print "Programming" from "PythonProgramming"
#======================================================
text = "PythonProgramming"
print(text[6:])


#=======================================
# Task 8: Print Every Third Character
#======================================= 
text = "Analytics"
print(text[::3])


#=========================================
# Task 9: Print "velop" from "Developer"
#========================================= 
text = "Developer"
print(text[2:7])


#=============================================
# Task 10: Print "World" from "Hello World"
#=============================================
text = "Hello World"
print(text[6:])


#===================================================
# Task 11: Print "Science" using Negative Indexing
#===================================================
text = "DataScience"
print(text[-7:])


#==============================================
# Task 12: Reverse the String Using Step Value
#==============================================
text = "Python"
print(text[::-1])


#=======================================
# Task 13: Print Characters with Step 2
#=======================================
text = "Programming"
print(text[1::2])


#==========================================================
# Task 14: Print "Science" from "Data Science with Python"
#==========================================================
text = "Data Science with Python"
print(text[5:12])


#==================================================
#                    Summary
#==================================================
# ✔ String slicing is used to extract a specific part of a string.
# ✔ Syntax: string[start : stop : step]
# ✔ The start index is included.
# ✔ The stop index is excluded.
# ✔ The step value decides how many positions to move.
# ✔ Positive indexing starts from 0.
# ✔ Negative indexing starts from -1.
# ✔ We can extract words, characters, reverse strings, and skip characters.
# ✔ Reverse a string using [::-1].
# ✔ Every second character: [::2]
# ✔ Every third character: [::3]
# ✔ Slicing does not produce an IndexError if the stop index is greater than the string length.


# ========================================
# End of Topic
# ========================================
# ✔ Topic Completed Successfully.
# ✔ Next Topic: Escape Characters
# Happy Coding! 🚀