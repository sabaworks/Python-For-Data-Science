"""
===============================================
Topic: Conditions and Branching in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
===============================================
""" 

#==========================================================
# What are Conditions and Branching?
#==========================================================

# Conditions allow a program to make decisions.
# Branching means choosing different paths of execution
# based on whether a condition is True or False.


#==========================================================
# Why Do We Use Conditions and Branching?
#==========================================================

# ✔ To make decisions in a program.
# ✔ To execute different code based on conditions.
# ✔ To validate user input.
# ✔ To compare values.
# ✔ To automate decision making.
# ✔ To control the flow of a program.


#==========================================================
# Task 1 : Check Student ID
#==========================================================
student_id = 1001
if student_id == 1001:
    print("Correct ID")
else:
    print("Wrong ID")    


#==========================================================
# Task 2 : Verify Username
#==========================================================
username = "Saba"
if username == "Saba":
    print("Login Allowed")
else:
    print("Access Denied")    


#==========================================================
# Task 3 : Check Free Delivery Eligibility
#==========================================================
order_amount = 6500
if order_amount > 5000:
    print("Free Delivery")
else:
    print("Delivery Charges Applied")        


#==========================================================
# Task 4 : Monitor Water Level
#==========================================================
water_level = 15
if water_level < 20:
    print("Low Water Level!!")
else:
    print("Water Level Normal.")        


#==========================================================
# Task 5 : Check Scholarship Eligibility
#==========================================================
marks = 80
if marks >= 80:
    print("Scholarship Eligible")
else:
    print("Not Eligible")    


#==========================================================
# Task 6 : Check Free Entry Eligibility
#==========================================================
age = 5
if age <= 5:
    print("Free Entry")
else:
    print("Ticket Required")    


#==========================================================
# Task 7 : Check Bonus Eligibility
#==========================================================
salary = 50000
if salary > 30000:
    print("Bonus Approved")
else:
    print("No Bonus")    


#==========================================================
# Task 8 : Senior Citizen Discount
#==========================================================
age = 70
if age >= 60:
    print("Discount Available")
else:
    print("Regular Price")    


#==========================================================
# Task 9 : Validate Coupon Code
#==========================================================
coupon_code = "ABC123"
if coupon_code == "SAVE50":
    print("Discount Applied")
else:
    print("Invalid Coupon")


#==========================================================
# Task 10 : Verify Employee ID
#==========================================================
employee_id = 7892
if employee_id != 9999:
    print("Entry Allowed")
else:
    print("Entry Blocked")


#==========================================================
# Task 11 : Check Account Balance
#==========================================================
balance = 5000
if balance >= 1000:
    print("Transaction Successful")
else:
    print("Insufficient Balance")


#==========================================================
# Task 12 : Assign Student Grade
#==========================================================
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")


#==========================================================
# Task 13 : Check Weather Condition
#==========================================================
temperature = 30 
if temperature >= 35:
    print("Hot")
elif temperature >= 20:
    print("Pleasant")
else:
    print("Cold")


#==========================================================
# Task 14 : Purchase Discount System
#==========================================================
purchase = 5000
if purchase >= 10000:
    print("20% Discount")
elif purchase >= 5000:
    print("10% Discount")
else:
    print("No Discount")


#==========================================================
# Task 15 : Complete Grading System
#==========================================================
marks = 75
if marks > 100 or marks < 0:
    print("Invalid Marks")
elif marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")


#==========================================================
# Task 16 : Bank Account Classification
#==========================================================
balance = 5000
if balance < 0:
    print("Invalid Balance")
elif balance >= 10000:
    print("Premium Account")
elif balance >= 5000:
    print("Standard Account")
elif balance >= 1000:
    print("Basic Account")
else:
    print("Low Balance")        


#==========================================================
# Task 17 : University Admission System
#==========================================================
age = 25
marks = 85
if age < 17 or age > 25:
    print("Not Eligible")
elif marks >= 90:
    print("Admission with 100% Scholarship")
elif marks >= 80:
    print("Admission with 50% Scholarship")            
elif marks >= 60:
    print("Admission Granted")
else:
    print("Admission Rejected")        


#==========================================================
# Task 18 : ATM Authentication (Nested If)
#==========================================================
entered_pin = 1234
if entered_pin == 1234:
    print("Check Finger Print")
    fingerprint_verified = True

    if fingerprint_verified:
        print("Access Granted")
    else:
        print("Fingerprint Verification Failed")
        
else:
    print("Invalid Pin")


#==========================================================
# Task 19 : Login and Dean's List Check
#==========================================================
login = True
if login:
    print("Login Successful")
    CGPA = 3.4

    if CGPA >= 3.5:
        print("Eligible for Dean's List")
    else:
        print("Not Eligible for Dean's List") 

else:
    print("Login Failed")        


#==========================================================
# Task 20 : Product Stock and Payment Verification
#==========================================================
product_status = "In Stock"
payment = "Success"

if product_status == "In Stock":
    print("Product in Stock")

    if payment == "Success":
        print("Order Placed Successfully")
    else:
        print("Payment Failed")

else:
    print("Product Out of Stock")


#==========================================================
# Summary
#==========================================================

# ✔ if is used to execute code when a condition is True.
# ✔ else executes when the condition is False.
# ✔ elif checks multiple conditions.
# ✔ Nested if places one if statement inside another.
# ✔ Comparison operators:
#     ==, !=, >, <, >=, <=
# ✔ Logical operators:
#     and, or, not
# ✔ Conditions and branching help programs make decisions.
# ✔ They improve the flexibility and control of a program.


#==========================================================
# End of Topic
#==========================================================

# Topic Completed Successfully
# Next Topic : Loops in Python 
# Happy Coding

