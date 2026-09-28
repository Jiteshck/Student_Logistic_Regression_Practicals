# Student Logistic Regression Practicals

This project contains two practical programs demonstrating **Logistic Regression** using Python and Scikit-learn.

The programs use student study hours as input and predict whether a student will **Pass or Fail**.

## 📌 Project Overview

* **Input:** Number of study hours
* **Output:** Student result
* `0` → Fail
* `1` → Pass

The project contains two practical programs:

1. Basic Logistic Regression
2. Logistic Regression with Train-Test Split and Accuracy Evaluation

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Logistic Regression
* Train-Test Split
* Accuracy Score

## 📂 Project Structure

```text
├── logistic_regression.py
├── logistic_regression_train_test.py
├── Student_Logistic_Regression_Practicals.pdf
└── README.md
```

## 📘 Practical 1 — Basic Logistic Regression

### File

`logistic_regression.py`

This program uses study hours to predict whether a student will pass or fail.

The Logistic Regression model is trained using the study-hour dataset and then predicts the result for a student who studied for **6 hours**.

It also displays the probability of:

* Fail
* Pass

### Concepts Covered

* Creating a dataset using NumPy
* Logistic Regression
* Model training
* Prediction
* Prediction probability

## 📗 Practical 2 — Train-Test Split and Accuracy

### File

`logistic_regression_train_test.py`

This program extends the basic Logistic Regression practical by splitting the dataset into training and testing data.

The model is trained using **80% of the data** and tested using the remaining **20%**.

It calculates the model's accuracy and predicts the result and probability for a new student who studied for **7 hours**.

### Concepts Covered

* `train_test_split()`
* Model training
* Test data prediction
* `accuracy_score()`
* Prediction probability

## 🔄 Workflow

```text
Student Study Hours
        ↓
Dataset
        ↓
Logistic Regression
        ↓
Pass / Fail Prediction
```

For the second practical:

```text
Dataset
   ↓
Train-Test Split
   ↓
Training Data
   ↓
Logistic Regression
   ↓
Test Data
   ↓
Prediction
   ↓
Accuracy
```

## 🎯 Learning Outcomes

This practical demonstrates:

* Understanding Logistic Regression
* Classification using Python
* Training a machine learning model
* Making predictions
* Predicting probabilities
* Splitting data into training and testing sets
* Evaluating model accuracy

## 📄 Practical Documentation

The complete code and outputs are available in:

`Student_Logistic_Regression_Practicals.pdf`


