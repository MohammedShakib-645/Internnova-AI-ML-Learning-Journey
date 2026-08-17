# Task 4 - First Machine Learning Model
# Mohammed Shakib | Week 3 | AI & Machine Learning

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

print("Task 4 - First Machine Learning Model (Logistic Regression)")
print()

df = pd.read_csv("../Dataset.csv")

# features and target
X = df[["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score", "Project_Score"]]
y = df["Result"]

# encode PASS/FAIL to 1/0
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# train model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)
print("Model trained!")
print()

# predict
y_pred = model.predict(X_test_scaled)

# actual vs predicted
print("Actual vs Predicted (first 10 test rows):")
print(f"{'Actual':<10} {'Predicted'}")
for a, p in zip(y_test[:10], y_pred[:10]):
    print(f"{le.inverse_transform([a])[0]:<10} {le.inverse_transform([p])[0]}")
print()

# accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc * 100:.2f}%")
print()

# confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
print()

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["FAIL", "PASS"]))

# save confusion matrix chart
fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(cm, cmap="Blues")
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(["FAIL", "PASS"])
ax.set_yticklabels(["FAIL", "PASS"])
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title("Confusion Matrix")
for i in range(2):
    for j in range(2):
        ax.text(j, i, str(cm[i][j]), ha="center", va="center", fontsize=14)
plt.colorbar(im)
plt.tight_layout()
plt.savefig("../Screenshots/confusion_matrix.png")
print("Saved: Screenshots/confusion_matrix.png")
print()

print("Done - Task 4 complete!")
