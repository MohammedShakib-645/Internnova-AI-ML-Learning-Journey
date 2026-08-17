# Task 2 - Pandas and Dataset Handling
# Mohammed Shakib | Week 2 Assignment

import pandas as pd

# pandas is used to work with datasets - loading, viewing and filtering data
# CSV files can be easily read using pd.read_csv()

print("Task 2 - Pandas and Dataset Handling")
print()

# loading the dataset
df = pd.read_csv("student_performance.csv")

# showing the full dataframe
print("Full Dataset:")
print(df)
print()

# first 5 rows
print("First 5 rows:")
print(df.head())
print()

# last 5 rows
print("Last 5 rows:")
print(df.tail())
print()

# shape - rows and columns
print("Number of rows and columns:", df.shape)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print()

# column names
print("Column names:")
print(df.columns.tolist())
print()

# data types of each column
print("Data types:")
print(df.dtypes)
print()

# basic statistics using describe
print("Basic Statistical Summary:")
print(df.describe())
print()

# selecting specific columns only
print("Selecting Name, Math, Science, English columns:")
print(df[["Name", "Math", "Science", "English"]])
print()

# filtering - students with Math marks greater than 70
print("Students with Math marks > 70:")
print(df[df["Math"] > 70][["Student_ID", "Name", "Math"]])
print()

# filtering - students with attendance 80 or above
print("Students with Attendance >= 80:")
print(df[df["Attendance"] >= 80][["Student_ID", "Name", "Attendance"]])
print()

print("Done - Task 2 complete!")
