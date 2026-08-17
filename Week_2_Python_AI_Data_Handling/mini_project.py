# Mini Project - Student Performance Data Analysis
# Mohammed Shakib | Week 2 Assignment

import matplotlib
matplotlib.use("Agg")  # non-interactive backend for saving charts
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

print("Mini Project - Student Performance Data Analysis")
print()

# -------------------------------------------------------
# Section 1 - Data Handling
# -------------------------------------------------------
print("--- Data Handling ---")
print()

df = pd.read_csv("student_performance.csv")

print("Dataset:")
print(df)
print()

print("Shape (rows, columns):", df.shape)
print()

print("Column names:")
print(df.columns.tolist())
print()

print("Data types:")
print(df.dtypes)
print()

print("Basic statistics:")
print(df.describe())
print()

# -------------------------------------------------------
# Section 2 - Data Cleaning
# -------------------------------------------------------
print("--- Data Cleaning ---")
print()

print("Missing values:")
print(df.isnull().sum())
print()

# no missing values in student_performance.csv but we still check
if df.isnull().sum().sum() == 0:
    print("No missing values found.")
else:
    df = df.dropna()
    print("Missing values removed.")
print()

print("Duplicate rows:", df.duplicated().sum())
if df.duplicated().sum() > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")
else:
    print("No duplicates found.")
print()

print("Dataset after cleaning:")
print(df)
print()

# -------------------------------------------------------
# Section 3 - Data Analysis
# -------------------------------------------------------
print("--- Data Analysis ---")
print()

# creating Average column from Math, Science, English
df["Average"] = (df["Math"] + df["Science"] + df["English"]) / 3
df["Average"] = df["Average"].round(2)

# creating Result column based on average >= 40
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("Dataset with Average and Result columns:")
print(df[["Student_ID", "Name", "Math", "Science", "English", "Average", "Result"]])
print()

# average marks
overall_avg = df["Average"].mean()
print(f"Average marks of all students: {overall_avg:.2f}")
print()

# highest and lowest
highest = df["Average"].max()
lowest = df["Average"].min()
print(f"Highest average marks: {highest}")
print(f"Lowest average marks : {lowest}")
print()

# pass and fail count
pass_count = len(df[df["Result"] == "Pass"])
fail_count = len(df[df["Result"] == "Fail"])
print(f"Number of students who passed: {pass_count}")
print(f"Number of students who failed: {fail_count}")
print()

# highest and lowest performing student
top_student = df.loc[df["Average"].idxmax(), "Name"]
low_student = df.loc[df["Average"].idxmin(), "Name"]
print(f"Highest performing student: {top_student}")
print(f"Lowest performing student : {low_student}")
print()

# best subject based on average
subject_avgs = {
    "Math": df["Math"].mean(),
    "Science": df["Science"].mean(),
    "English": df["English"].mean()
}
best_subject = max(subject_avgs, key=subject_avgs.get)
print("Average marks per subject:")
for subj, avg in subject_avgs.items():
    print(f"  {subj}: {avg:.2f}")
print(f"Best performing subject: {best_subject}")
print()

# average attendance
avg_attendance = df["Attendance"].mean()
print(f"Average attendance: {avg_attendance:.2f}%")
print()

# -------------------------------------------------------
# Section 4 - Visualizations
# -------------------------------------------------------
print("--- Creating Visualizations ---")
print()

# chart 1 - student average marks bar chart
plt.figure(figsize=(12, 5))
plt.bar(df["Name"], df["Average"], color="cornflowerblue")
plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/mini_project_average.png")
plt.show()
print("Saved: outputs/mini_project_average.png")

# chart 2 - average marks by subject
plt.figure(figsize=(6, 5))
plt.bar(subject_avgs.keys(), subject_avgs.values(), color=["steelblue", "mediumseagreen", "tomato"])
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("outputs/subject_average.png")
plt.show()
print("Saved: outputs/subject_average.png")

# chart 3 - pass vs fail pie chart
plt.figure(figsize=(5, 5))
plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct="%1.1f%%",
        colors=["mediumseagreen", "tomato"], startangle=90)
plt.title("Pass vs Fail Distribution")
plt.tight_layout()
plt.savefig("outputs/pass_fail.png")
plt.show()
print("Saved: outputs/pass_fail.png")
print()

# -------------------------------------------------------
# Section 5 - Insights and Conclusion
# -------------------------------------------------------
print("--- Insights ---")
print()
print(f"1. The overall average marks of all students is {overall_avg:.2f}.")
print(f"2. {top_student} performed the best with an average of {highest}.")
print(f"3. {low_student} had the lowest average of {lowest}.")
print(f"4. Out of {len(df)} students, {pass_count} passed and {fail_count} failed.")
print(f"5. {best_subject} was the best performing subject with an average of {subject_avgs[best_subject]:.2f}.")
print(f"6. Average class attendance was {avg_attendance:.2f}%.")
print()

print("--- Conclusion ---")
print()
print(f"This project analyzed the performance of {len(df)} students across three subjects.")
print(f"The overall class average was {overall_avg:.2f} marks. {top_student} was the top")
print(f"performer while {low_student} needs more support. A total of {pass_count} students")
print(f"passed and {fail_count} failed based on the 40-mark threshold. {best_subject} had")
print(f"the highest subject average of {subject_avgs[best_subject]:.2f}. The class attendance")
print(f"averaged {avg_attendance:.2f}% which is fairly good. The visualizations clearly showed")
print("how marks are distributed and which students need improvement. This project helped")
print("understand how to use Python libraries like Pandas and Matplotlib to analyze real data.")
print()

print("Done - Mini Project complete!")
