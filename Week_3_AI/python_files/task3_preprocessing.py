# Task 3 - Train-Test Split and Preprocessing
# Mohammed Shakib | Week 3 | AI & Machine Learning

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("Task 3 - Train-Test Split and Preprocessing")
print()

df = pd.read_csv("../Dataset.csv")

X = df[["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score", "Project_Score"]]
y = df["Result"]

# split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])
print()

print("X_train shape:", X_train.shape)
print("X_test shape :", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape :", y_test.shape)
print()

print("Why split? So the model doesn't just memorize answers.")
print("We test on data it has never seen to check real performance.")
print()

# scaling features using StandardScaler
# we fit only on training data to avoid data leakage
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaling done. Scaler fitted on training data only.")
print()

print("Done - Task 3 complete!")
