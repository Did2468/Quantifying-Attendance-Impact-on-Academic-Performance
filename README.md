# 📊 Attendance vs SGPA Performance Analysis

## 🎯 Project Overview

This project investigates **how university classroom attendance influences academic performance (SGPA)**. Unlike typical ML demo projects using public Kaggle datasets, this project is based on **real student data collected manually** from my university. The goal is to derive **actionable and evidence-based insights** that can support academic decision‑making and student guidance.

The project uses **statistical modeling, exploratory data analysis, and regression** to study the relationship between attendance percentage and SGPA for **200 students over two semesters**.

📍 Data Collection Challenges

Collecting the dataset required manually compiling attendance records and SGPA values for students, as automated export was not available. Each student’s record had to be queried individually, cleaned, and standardized due to inconsistencies in formatting and missing fields. This process reinforced real-world skills such as dealing with imperfect data, handling missing values, and structuring datasets from unorganized sources.

## ❓ Problem Statement

> **Does attending classes significantly impact academic performance?** Can attendance alone be used to estimate or forecast SGPA and have any significant impact?

Universities enforce attendance policies (e.g., 75%) without presenting measurable evidence. This project aims to quantify that impact scientifically with help of real data.

---

## 📦 Dataset Description

| Attribute       | Description                    |
| --------------- | ------------------------------ |
| `sem1_attended` | Classes attended in Semester 1 |
| `sem1_total`    | Total classes in Semester 1    |
| `sgpa1`         | Semester 1 SGPA                |
| `sem2_attended` | Classes attended in Semester 2 |
| `sem2_total`    | Total classes in Semester 2    |
| `sgpa2`         | Semester 2 SGPA                |

### Derived Features

```
sem1_attendance = (sem1_attended / sem1_total) * 100
sem2_attendance = (sem2_attended / sem2_total) * 100
```

Dataset size: **200 students**

---

## 🛠 Techniques & Tools Used

- Python, Pandas, NumPy, Matplotlib, Seaborn
- Scikit‑Learn (linear & polynomial regression)
- Data cleaning and feature engineering
- Correlation analysis and visualization
- Model evaluation using R² & RMSE
- Modular project structure with `/src`, `/data`, `/results`

---

## 📈 Exploratory Data Analysis

Key plots generated:

- Attendance distribution
- SGPA distribution
- Scatter plots with regression trendlines
- Correlation heatmap

> \*\*All generated figures are available in \results``

---

## 🧠 Regression Model Results

### **Semester 1 — Linear Regression**

```
SGPA = -1.835 + 0.105 * Attendance
R² = 0.3188
```

### **Semester 2 — Linear Regression**

```
SGPA = -3.437 + 0.125 * Attendance
R² = 0.2434
```

### Interpretation

- **Attendance alone explains \~32% of SGPA variation (Sem1) and \~24% (Sem2)**
- **Every +10% attendance ≈ +1.0 to +1.2 SGPA increase**
- **Polynomial regression does not significantly outperform linear models** (indicating stable linear relationship)

---

## 🧾 Key Insights & Conclusions

### 📍 Major Findings

- Attendance has a **strong positive correlation** with SGPA (0.56 Sem1, 0.49 Sem2)
- **Attendance is a significant single predictor** of academic performance
- **32% contribution from one variable is statistically large** given academic performance depends on many factors
- Simple linear model provides **clear interpretability and actionable guidance**

### 🎯 Actionable Recommendations

- Students should maintain **>80% attendance** to maximize academic outcomes
- Universities can justify attendance policies using evidence instead of assumptions

### 📌 Future Work

- Add additional predictors (internals, study hours, difficulty scores)
- Convert into a **Streamlit dashboard tool** for student risk prediction
- Expand dataset across departments and semesters
- Research publication with statistical rigor and confidence intervals

---

## 📂 Project Structure

```
project-root/
│
├── data/
├── notebooks/
├── src/
├── results
└── README.md
```

---

## 📬 Contact

If you found this analysis interesting or wish to collaborate on research: **Email:** [did79385@gmail.com]

---

## ⭐ Final Statement

> **This project demonstrates how simple statistical modeling on real‑world data can uncover meaningful academic insights that influence policy, student performance tracking, and decision‑making.**

> Real data. Real impact. Not a toy Kaggle model, but an actionable education analytics study.

