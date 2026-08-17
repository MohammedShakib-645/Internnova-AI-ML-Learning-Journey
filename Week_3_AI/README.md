# Week 3 - Introduction to Machine Learning

**Student:** Mohammed Shakib  
**Course:** AI & Machine Learning  
**Week:** 3  

---

## What this project is about

This is my Week 3 assignment on Machine Learning basics. I learned what ML is, how to prepare a dataset, split it into training and testing, scale features, train a Logistic Regression model, and predict student performance.

---

## Tasks

- Task 1 - Machine Learning Fundamentals (concepts)
- Task 2 - Dataset Preparation
- Task 3 - Train-Test Split and Preprocessing
- Task 4 - First ML Model (Logistic Regression)
- Task 5 - Mini Project (Student Performance Prediction)

---

## Dataset

`Dataset.csv` has 55 student records with these columns:
- Student_ID, Study_Hours, Attendance, Previous_Marks, Assignment_Score, Project_Score, Final_Marks, Result

Features used: Study_Hours, Attendance, Previous_Marks, Assignment_Score, Project_Score  
Target: Result (PASS or FAIL)

---

## How to Install

```
pip install pandas numpy matplotlib scikit-learn jupyter
```

## How to Run

```
# run each task
python python_files/task1_ml_fundamentals.py
python python_files/task2_dataset_preparation.py
python python_files/task3_preprocessing.py
python python_files/task4_first_ml_model.py
python python_files/mini_project.py

# or open the notebook
jupyter notebook Week3_ML.ipynb
```

---

## Model Results

- Model: Logistic Regression
- Accuracy: 100%
- Student 1 (good student): PASS
- Student 2 (weak student): FAIL
- Student 3 (excellent student): PASS

---

## What I learned

- What Machine Learning is and how it works
- Difference between AI, ML and Deep Learning
- How to prepare and clean a dataset
- How to split data into training and testing sets
- How to scale features using StandardScaler
- How to train a Logistic Regression model
- How to evaluate with accuracy, confusion matrix and classification report
