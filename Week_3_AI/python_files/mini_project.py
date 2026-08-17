# Mini Project - Student Performance Prediction
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

print("Mini Project - Student Performance Prediction")
print()

# load data
df = pd.read_csv("../Dataset.csv")
print("Dataset loaded. Shape:", df.shape)
print()

# check missing and duplicates
print("Missing values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())
print()

# features and target
X = df[["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score", "Project_Score"]]
y = df["Result"]

# encode target
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])
print()

# scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# train
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)
print("Model trained!")

# predict and evaluate
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc * 100:.2f}%")
print()
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["FAIL", "PASS"]))

# confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
print()

# --- 3 new student predictions ---
print("Predicting for 3 new students:")
print()

new_students = pd.DataFrame({
    "Study_Hours":      [6,   2,   8  ],
    "Attendance":       [85,  60,  95 ],
    "Previous_Marks":   [72,  42,  88 ],
    "Assignment_Score": [80,  50,  92 ],
    "Project_Score":    [78,  45,  90 ]
})

new_scaled = scaler.transform(new_students)
predictions = le.inverse_transform(model.predict(new_scaled))

for i in range(3):
    print(f"Student {i+1}: Study={new_students.iloc[i,0]}h, Attendance={new_students.iloc[i,1]}%,"
          f" Prev Marks={new_students.iloc[i,2]}, Assign={new_students.iloc[i,3]}, Project={new_students.iloc[i,4]}")
    print(f"  --> Prediction: {predictions[i]}")
    print()

# --- Charts ---

# chart 1 - pass vs fail
plt.figure(figsize=(5, 4))
y.value_counts().plot(kind="bar", color=["mediumseagreen", "tomato"])
plt.title("PASS vs FAIL Distribution")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../Screenshots/pass_fail_distribution.png")
print("Saved: pass_fail_distribution.png")

# chart 2 - scatter plot
plt.figure(figsize=(6, 5))
colors = ["tomato" if r == "FAIL" else "steelblue" for r in df["Result"]]
plt.scatter(df["Study_Hours"], df["Previous_Marks"], c=colors, s=60, alpha=0.7)
plt.title("Study Hours vs Previous Marks")
plt.xlabel("Study Hours")
plt.ylabel("Previous Marks")
plt.tight_layout()
plt.savefig("../Screenshots/scatter_study_vs_marks.png")
print("Saved: scatter_study_vs_marks.png")

# chart 3 - confusion matrix
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
plt.savefig("../Screenshots/mini_project_cm.png")
print("Saved: mini_project_cm.png")
print()

print("Done - Mini Project complete!")
