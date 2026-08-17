# Task 3 - Data Cleaning
# Mohammed Shakib | Week 2 Assignment

import pandas as pd

# in real life datasets are never perfect
# they have missing values, duplicate rows, and wrong data types
# this task is about finding and fixing all those issues

print("Task 3 - Data Cleaning")
print()

# loading the messy dataset
df = pd.read_csv("messy_student_data.csv")

# --- BEFORE CLEANING ---
print("Dataset BEFORE Cleaning:")
print(df)
print()

# checking missing values
print("Missing values in each column:")
print(df.isnull().sum())
print()

print("Total missing values:", df.isnull().sum().sum())
print()

# checking for duplicate rows
print("Duplicate rows found:", df.duplicated().sum())
print()

print("Duplicate rows:")
print(df[df.duplicated(keep=False)])
print()

# checking data types
print("Data types before cleaning:")
print(df.dtypes)
print()

# --- CLEANING PROCESS ---

# step 1 - removing duplicate rows
# keeping the first occurrence and dropping the rest
df = df.drop_duplicates()
print("After removing duplicates, rows remaining:", len(df))
print()

# step 2 - fixing the Age column
# some ages are written as words like 'twenty' or 'twenty-one'
# we convert them to numbers and anything that cant be converted becomes NaN
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
print("Age column after fixing wrong data types:")
print(df["Age"])
print()

# step 3 - filling missing values
# for numeric columns like marks and attendance we fill with the column average
# for Name we fill with 'Unknown' since we dont know the name
df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Age"] = df["Age"].fillna(df["Age"].median())  # using median for age because it's more suitable
df["Name"] = df["Name"].fillna("Unknown")

# rounding the filled values to keep them clean
df["Math"] = df["Math"].round(1)
df["Science"] = df["Science"].round(1)
df["English"] = df["English"].round(1)
df["Attendance"] = df["Attendance"].round(1)

# converting Age back to integer after filling
df["Age"] = df["Age"].astype(int)

# --- AFTER CLEANING ---
print("Dataset AFTER Cleaning:")
print(df)
print()

# verifying no missing values left
print("Missing values after cleaning:")
print(df.isnull().sum())
print()

# verifying no duplicates left
print("Duplicate rows after cleaning:", df.duplicated().sum())
print()

# final data types
print("Data types after cleaning:")
print(df.dtypes)
print()

print("Done - Task 3 complete!")
