# Task 4 - Data Visualization
# Mohammed Shakib | Week 2 Assignment

import matplotlib
matplotlib.use("Agg")  # use non-interactive backend so charts save without needing a display
import pandas as pd
import matplotlib.pyplot as plt
import os

# making sure the outputs folder exists to save graphs
os.makedirs("outputs", exist_ok=True)

# loading the dataset
df = pd.read_csv("student_performance.csv")

print("Task 4 - Data Visualization")
print("Creating 4 charts...")
print()

# -------------------------------------------------------
# Chart 1 - Bar Chart: Students vs Math Marks
# -------------------------------------------------------
plt.figure(figsize=(12, 5))
plt.bar(df["Name"], df["Math"], color="steelblue")
plt.title("Students vs Math Marks")
plt.xlabel("Student Name")
plt.ylabel("Math Marks")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/bar_chart.png")
plt.show()
print("Bar chart saved as outputs/bar_chart.png")
print()

# -------------------------------------------------------
# Chart 2 - Line Chart: Students vs Science Marks
# -------------------------------------------------------
plt.figure(figsize=(12, 5))
plt.plot(df["Name"], df["Science"], marker="o", color="green", linewidth=2)
plt.title("Students vs Science Marks")
plt.xlabel("Student Name")
plt.ylabel("Science Marks")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/line_chart.png")
plt.show()
print("Line chart saved as outputs/line_chart.png")
print()

# -------------------------------------------------------
# Chart 3 - Histogram: Distribution of Math Marks
# -------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["Math"], bins=8, color="orange", edgecolor="black")
plt.title("Distribution of Math Marks")
plt.xlabel("Math Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("outputs/histogram.png")
plt.show()
print("Histogram saved as outputs/histogram.png")
print()

# -------------------------------------------------------
# Chart 4 - Scatter Plot: Math vs Science Marks
# -------------------------------------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df["Math"], df["Science"], color="purple", s=80)
plt.title("Math vs Science Marks")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.tight_layout()
plt.savefig("outputs/scatter_plot.png")
plt.show()
print("Scatter plot saved as outputs/scatter_plot.png")
print()

print("Done - Task 4 complete! All charts saved in outputs/ folder")
