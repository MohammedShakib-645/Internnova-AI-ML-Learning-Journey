# Task 1 - NumPy Fundamentals
# Mohammed Shakib | Week 2 Assignment

import numpy as np

# what is numpy - its basically a python library for working with numbers and arrays
# very useful in AI and data science because it makes calculations fast and easy

print("Task 1 - NumPy Fundamentals")
print()

# creating a 1D array - just a simple list of marks
marks = np.array([85, 72, 90, 55, 40, 78, 95, 35, 62, 88])
print("1D Array (Math Marks):")
print(marks)
print()

# creating a 2D array - rows are students, columns are subjects (Math, Science, English)
marks_2d = np.array([
    [85, 78, 82],
    [72, 68, 75],
    [90, 95, 88],
    [55, 60, 65],
    [40, 45, 50],
    [78, 80, 72],
    [95, 92, 90],
    [35, 40, 38],
    [62, 58, 70],
    [88, 85, 80]
])
print("2D Array (Math, Science, English for 10 students):")
print(marks_2d)
print()

# indexing - accessing a specific element
print("Array Indexing:")
print("First student mark (index 0):", marks[0])
print("Last student mark (index -1):", marks[-1])
print("Third student, Science marks (row 2, col 1):", marks_2d[2][1])
print()

# slicing - getting a portion of the array
print("Array Slicing:")
print("Students 2 to 5 marks:", marks[2:6])
print("First 3 students all subjects:")
print(marks_2d[0:3])
print("Math column for all students:", marks_2d[:, 0])
print()

# shape tells us how many rows and columns
print("Shape of 1D array:", marks.shape)
print("Shape of 2D array:", marks_2d.shape)
print()

# ndim tells number of dimensions
print("Dimensions in 1D array:", marks.ndim)
print("Dimensions in 2D array:", marks_2d.ndim)
print()

# basic math operations
print("Math Operations on marks array:")
print("Original:", marks)
print("Add 5 to each:", marks + 5)
print("Subtract 5:", marks - 5)
print("Multiply by 2:", marks * 2)
print("Divide by 2:", marks / 2)
print()

# statistical functions
print("Statistical Functions:")
print("Mean (average):", marks.mean())
print("Max (highest):", marks.max())
print("Min (lowest):", marks.min())
print("Sum (total):", marks.sum())
print()

print("Done - Task 1 complete!")
