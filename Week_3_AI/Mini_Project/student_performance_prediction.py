# Student Performance Prediction - Mini Project
# Mohammed Shakib | Week 3 | AI & Machine Learning
# Run this file from the Mini_Project folder

import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import os

os.makedirs("../Screenshots", exist_ok=True)

print("Student Performance Prediction")
print()

df = pd.read_csv("Dataset.csv")
print("Dataset shape:", df.shape)

X = df[["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score", "Project_Score"]]
y = df["Result"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {acc * 100:.2f}%")
print()
print(classification_report(y_test, y_pred, target_names=["FAIL", "PASS"]))

# 3 new students
new_students = pd.DataFrame({
    "Study_Hours":      [6,   2,   8  ],
    "Attendance":       [85,  60,  95 ],
    "Previous_Marks":   [72,  42,  88 ],
    "Assignment_Score": [80,  50,  92 ],
    "Project_Score":    [78,  45,  90 ]
})

new_pred = le.inverse_transform(model.predict(scaler.transform(new_students)))
for i, p in enumerate(new_pred):
    print(f"Student {i+1} --> {p}")

print()
print("Done!")
