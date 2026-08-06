"""
===============================================
Topic: Exception Handling in Python

Course:
IBM Python for Data Science, AI & Development

Author: Saba Ishaq
===============================================
""" 

#============================================================
# Question 1: What is Exception Handling?
#============================================================
# Exception Handling is a technique used to detect and
# handle runtime errors in a program. It prevents the
# program from crashing and allows it to continue
# executing gracefully.
# Examples:
# - ZeroDivisionError
# - ValueError
# - TypeError
# - NameError
# - IndexError
# - FileNotFoundError



#============================================================
# Question 2: Why Do We Use Exception Handling?
#============================================================
# We use Exception Handling to:

# ✔ Prevent program crashes.
# ✔ Handle unexpected runtime errors.
# ✔ Display user-friendly error messages.
# ✔ Improve program reliability.
# ✔ Validate user input.
# ✔ Ensure important code always executes using finally.

#============================================================
# Syntax
#============================================================

# try:
    # Code that may cause an exception

# except ExceptionType:
    # Handle the exception

# else:
    # Executes if no exception occurs

# finally:
    # Always executes


#============================================================
# # Keywords Used
#============================================================
# try      -> Contains risky code.
# except   -> Handles the exception.
# else     -> Runs if no exception occurs.
# finally  -> Always executes.
# raise    -> Creates a custom exception.
# as e     -> Stores the exception message.


#============================================================
# # Flow of Exception Handling
#============================================================
#           Start
#             ↓
#          try Block
#             ↓
#         Exception?
#          /      \
#         Yes     No
#         |       |
#      except    else
#          \    /
#          finally
#             ↓
#            End


#============================================================
# Task 1: Validate User Age
#============================================================

try:
    age = int(input("Enter your age: "))
    if age < 0:
     raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(e)
else:
    print("Welcome!")    
finally:
    print("Program Ended")

#============================================================
# Task 2: Convert Temperature from Celsius to Fahrenheit 🌡️
#============================================================

try:
    temp_celcius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (temp_celcius * 9/5) + 32
    if temp_celcius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
except ValueError as e:
    print("Invalid input:", e)
else:
    print(fahrenheit, "°F")
finally:
    print("Conversion Completed")        


#============================================================
# Task 3: Calculate the Area of a Rectangle
#============================================================

try:
    length = float(input("Enter length in meters: "))
    width = float(input("Enter width in meters: "))
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    if length == 0 or width == 0:
        raise ValueError("Length and width cannot be zero.")
except ValueError as e:
    print("Invalid input:", e)
else:
    print("Area of the rectangle:", length * width)
finally:
    print("Calculation Completed")


#============================================================
# Task 4: Calculate Employee Salary and Tax
#============================================================

try:
    basic_salary = float(input("Enter basic salary: "))
    if basic_salary < 0:
        raise ValueError("Salary cannot be negative.")
except ValueError as e:
    print("Invalid input:", e)
else:
    tax = basic_salary * 0.10
    print("Tax Amount:", tax)
    print("Net Salary:", basic_salary - tax)
finally:
    print("Salary Process Completed")

#============================================================
# Task 5: Verify Voting Eligibility
#============================================================

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
except ValueError as e:
    print("Invalid input:", e)
else:
    print("You are eligible to vote.")
finally:
    print("Verification Completed")

#============================================================
# Task 6: Generate an Electricity Bill
#============================================================

try:
    consumed_units = int(input("Enter consumed units: "))
    if consumed_units < 0:
        raise ValueError("Consumed units cannot be negative.")
except ValueError as e:
    print("Invalid input:", e)
else:
    print("Bill :", consumed_units * 25)
finally:
    print("Bill Generated Successfully")


#============================================================
# Task 7: Calculate the Total Product Price
#============================================================

try:
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price_per_item = float(input("Enter price per item: "))
    if not product_name.strip():
        raise ValueError("Product name cannot be empty.")
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if price_per_item < 0:
        raise ValueError("Price per item cannot be negative.")
except ValueError as e:
    print("Invalid input:", e)
else:
    total_price = quantity * price_per_item
    print("Total Price:", total_price)
finally:
    print("Order Process Completed")


#============================================================
# Task 8: Manage Student Fee Records
#============================================================

try:
    student_name = input("Enter student name: ")
    fee_amount = float(input("Enter fee amount: "))
    paid_amount = float(input("Enter paid amount: "))
    if not student_name.strip():
        raise ValueError("Student name cannot be empty.")
    if fee_amount < 0 or paid_amount < 0:
        raise ValueError("Fee and paid amounts cannot be negative.")
    if paid_amount > fee_amount:
        raise ValueError("Paid amount cannot exceed fee amount.")
except ValueError as e:
    print("Invalid input:", e)
else:
    remaining_fee = fee_amount - paid_amount
    print("Remaining Fee:", remaining_fee)
finally:
    print("Fee Record Updated")


#============================================================
# Task 9: Calculate Hotel Booking Bill
#============================================================

try:
    guest_name = input("Enter guest name: ")
    room_number = int(input("Enter room number: "))
    number_of_days = int(input("Enter number of days: "))
    if not guest_name.strip():
        raise ValueError("Guest name cannot be empty.")
    if room_number <= 0 or number_of_days <= 0:
        raise ValueError("Room number and number of days must be positive.")
except ValueError as e:
    print("Invalid input:", e)
else:
    total_bill = number_of_days * 5000
    print("Total Bill:", total_bill)
finally:
    print("Booking Completed")


#============================================================
# Task 10: Mobile Recharge Validation
#============================================================

try:
    mobile_number = int(input("Enter mobile number: "))
    recharge_amount = float(input("Enter recharge amount: "))
    if len(str(mobile_number)) != 11 or not str(mobile_number).isdigit():
        raise ValueError("Mobile number must contain exactly 11 digits.")
    if recharge_amount < 100:
        raise ValueError("Recharge amount must be at least 100.")
except ValueError as e:
    print("Invalid input:", e)
else:
    print("Recharge Successful")
finally:    
    print("Transaction Completed")


#============================================================
# Task 11: Validate File Download
#============================================================

try:
    file_size = int(input("Enter file size in MB: "))
    available_storage = int(input("Enter available storage in MB: "))
    if file_size < 0 or available_storage < 0:
        raise ValueError("File size and available storage cannot be negative.")
    if file_size > available_storage:
        raise ValueError("File size exceeds available storage.")
except ValueError as e:
    print("Invalid input:", e)
else:
    remaining_storage = available_storage - file_size
    print("Download Started")
    print("Remaining Storage:", remaining_storage)
finally:
    print("Download Process Finished")    
    
    
#============================================================
# Task 12: Course Enrollment System
#============================================================

try:
    student_name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course_fee = float(input("Enter course fee: "))
    wallet_balance = float(input("Enter wallet balance: "))
    if not student_name.strip():
        raise ValueError("Student name cannot be empty.")
    if age < 16:
        raise ValueError("Student must be at least 16 years old.")
    if course_fee < 0 or wallet_balance < 0:
        raise ValueError("Course fee and wallet balance cannot be negative.")
    if course_fee > wallet_balance:
        raise ValueError("Course fee exceeds wallet balance.")
except ValueError as e:
    print("Invalid input:", e)
else:
    remaining_balance = wallet_balance - course_fee
    print("Enrollment Successful")
    print("Remaining Balance:", remaining_balance)
finally:
    print("Enrollment Process Completed")


#============================================================
# Task 13: Handle Division by Zero
#============================================================

try:
    num1 = int(input("Enter a Number: "))
    num2 = int(input("Enter a Number: "))
    print(num1 / num2)
except ZeroDivisionError:    
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter numbers only.")
finally:
    print("Program Finished")


#============================================================
# Task 14: Student Grading System
#============================================================

try:
    marks = int(input("Enter your marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")
    if marks >= 90:
            print("Grade A")
    elif marks >= 80:
            print("Grade B")
    elif marks >= 70:
            print("Grade C")
    elif marks >= 60:
            print("Grade D")
    else:
            print("Fail")
except ValueError as e:
    print(e)
finally:
    print("Result Process Completed")                        


#============================================================
# Task 15: ATM Withdrawal System
#============================================================

try:
    acc_balance = int(input("Enter Your Account Balance: "))
    withdraw_amount = int(input("Enter the Amount to Withdraw: "))
    if withdraw_amount < 0:
        raise ValueError("Withdraw amount cannot be negative.")
    if withdraw_amount > acc_balance:
        raise ValueError("Insufficient funds.")
except ValueError as e:
    print(e)
else:
    print("Your Remaining Balance is: ", acc_balance - withdraw_amount)
finally:
     print("Thank you for using our ATM.")


#============================================================
# Task 16: User Login Authentication
#============================================================

username = "admin"
password = "12345"

try:
    if username != "admin" or password != "12345":
        raise ValueError("Invalid Username or Password")
except ValueError as e:
    print(e)
else:
    print("Login Successful!")
finally:
    print("Login process completed.")
     

#============================================================
# Task 17: Student Registration System
#============================================================

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    cgpa = float(input("Enter your CGPA: "))
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if cgpa <0 or cgpa > 4.0:
        raise ValueError("CGPA should be between 0 and 4.0.")
except ValueError as e:
    print("Invalid input:", e)     
else:
    print("Registration Successful")    
finally:
    print("Student Registration Process Completed")    


#============================================================
# Task 18: Library Book Issue System
#============================================================

try:
    book_name = input("Enter the book name: ")
    copies = int(input("Enter the number of copies: "))
    borrowed = int(input("Enter the number of borrowed copies: "))
    if not book_name.strip():
        raise ValueError("Book name cannot be empty.")
    if copies < 0:
        raise ValueError("Number of copies cannot be negative.")
    if borrowed <= 0:
        raise ValueError("Borrowed copies cannot be zero or negative.")
    if borrowed > copies:
        raise ValueError("Borrowed copies cannot exceed total copies.")
except ValueError as e:
    print("Invalid input:", e)
else:
    print("Book Issued Successfully")
    print("Remaining Copies: ", copies - borrowed)
finally:
    print("Library Transaction Completed")


#============================================================
# Task 19: Calculate Product Discount
#============================================================

try:
    price = int(input("Enter Price "))
    discount = int(input("Enter Discount "))
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if discount < 0 or discount > 100:
        raise ValueError("Discount should be between 0 and 100.")
except ValueError as e:
    print("Invalid input:", e)    
else:
    final_price = price - (price * discount / 100)
    print("Final Price after Discount: ", final_price)
finally:
    print("Price Calculation Completed")        


#============================================================
# Task 20: Bank Account Management System
#============================================================

try:
    customer_name = input("Enter Customer Name: ")
    account_number = input("Enter Account Number: ")
    account_balance = float(input("Enter Account Balance: "))
    transaction_amount = float(input("Enter Transaction Amount: "))
    if not customer_name.strip():
        raise ValueError("Customer name cannot be empty.")
    if len(str(account_number)) != 10 or not str(account_number).isdigit():
        raise ValueError("Account number must contain exactly 10 digits.")
    if account_balance < 0:
        raise ValueError("Account balance cannot be negative.")
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be positive.")
    if transaction_amount > account_balance:
        raise ValueError("Insufficient funds for the transaction.")
except ValueError as e:
    print("Invalid input:", e)
else:
    print("Transfer Successful")
    print("Remaining Balance: ", account_balance - transaction_amount)
finally:
    print("Transaction Completed")


#============================================================
# Summary
#============================================================

# ✔ Exception Handling prevents program crashes.
# ✔ try contains the risky code.
# ✔ except handles errors.
# ✔ else executes when no exception occurs.
# ✔ finally always executes.
# ✔ raise is used to create custom exceptions.
# ✔ ValueError handles invalid values.
# ✔ ZeroDivisionError handles division by zero.
# ✔ Exception Handling improves program reliability.
# ✔ It makes programs more user-friendly and robust.


#============================================================
# End of Topic
#============================================================

# ✔ Topic Completed Successfully.
# ✔ Next Topic: Object-Oriented Programming (OOP)
# Happy Coding! 🚀

