# Task 3 - Python for AI
# Pass/Fail Prediction

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

print("\nStudent Name:", name)
print("Marks:", marks)
print("Data Type of marks:", type(marks))

if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Prediction:", result)
