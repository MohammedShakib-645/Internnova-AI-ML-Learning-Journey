# Task 2 - Dataset Preparation
# Mohammed Shakib | Week 3 | AI & Machine Learning

import pandas as pd

print("Task 2 - Dataset Preparation")
print()

df = pd.read_csv("../Dataset.csv")

print("First 5 rows:")
print(df.head())
print()

print("Last 5 rows:")
print(df.tail())
print()

print("Shape:", df.shape)
print()

print("Column names:")
print(df.columns.tolist())
print()

print("Data types:")
print(df.dtypes)
print()

print("Missing values:")
print(df.isnull().sum())
print()

print("Duplicate rows:", df.duplicated().sum())
print()

print("Statistical summary:")
print(df.describe())
print()

print("Features (X) - what we use to predict:")
print(["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score", "Project_Score"])
print()

print("Target (y) - what we want to predict:")
print("Result column (PASS or FAIL)")
print()

print("Note: Student_ID is not used as a feature.")
print("It is just an identifier and has no useful information for prediction.")
print()

X = df[["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score", "Project_Score"]]
y = df["Result"]

print("X shape:", X.shape)
print("y value counts:")
print(y.value_counts())
print()

print("Done - Task 2 complete!")
