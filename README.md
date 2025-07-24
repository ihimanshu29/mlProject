# 🎓 Student Maths Score Predictor

A modern Machine Learning web application that predicts a student’s **maths score** based on various academic and personal input features. Built using **Python**, **Scikit-learn**, **Flask**, **Docker**, and deployed on **Render** with a sleek **Tailwind CSS** frontend.

---

## 🚀 Live Demo

🌐 [Click here to open the live app](https://student-churn-prediction.onrender.com/)

---

## 📌 Project Overview

This project showcases an end-to-end ML solution — from **data preprocessing**, **model training**, to **real-time prediction** via a web interface. It solves a regression problem in the education domain, predicting students' maths scores based on multiple factors.

---

## 🧠 ML Model Info

- **Model Type:** Regression
- **Algorithm:** Linear Regression (or update based on your actual model)
- **Target Variable:** `math_score`
- **Example Input Features:**
  - Hours Studied
  - Previous Test Scores
  - Parental Education
  - Study Method
  - School Support

---

## 🛠 Tech Stack

| Area        | Tools Used                         |
|-------------|------------------------------------|
| **Backend** | Flask, Python, Scikit-learn        |
| **Frontend**| HTML, Tailwind CSS                 |
| **ML**      | Pandas, NumPy, Sklearn             |
| **Deployment** | Docker, Render.io              |

---

## 📁 Folder Structure
```text
├── .github
│   └── workflows
├── README.md
├── app.py
├── catboost_info
│   ├── learn
│   └── tmp
├── logs
├── mlproject.egg-info
├── notebook
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data
├── print_my_code_tree.py
├── setup.py
├── src
│   ├── __init__.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── exception.py
│   ├── logger.py
│   ├── pipelines
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   └── utils.py
├── templates
│   ├── index.html
│   └── home.html
├── Dockerfile
├── requirements.txt
└── README.md



