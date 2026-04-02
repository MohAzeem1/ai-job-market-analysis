# 🚀 AI Job Market Salary Prediction

## 📌 Project Overview

This project focuses on analyzing the AI job market dataset and building a Machine Learning model to predict salaries based on various factors like experience level, job role, skills, and company details.

The goal is to understand **what actually drives salary in the AI industry** and build a reliable prediction model.

---

## 📊 Exploratory Data Analysis (EDA)

During EDA, we explored the dataset step by step:

* Checked missing values and data types
* Analyzed distribution of salary using histograms
* Compared salary across different countries
* Studied salary variation by job roles and experience levels
* Visualized relationships using boxplots and scatterplots

### 🔍 Key Observations:

* Salary distribution is slightly right-skewed
* Senior-level roles have significantly higher salaries
* Job roles like **Machine Learning Engineer** and **AI Engineer** tend to earn more
* Country-wise salary differences are present but not extreme
* Surprisingly, **years of experience did not show a strong trend**

---

## 🔗 Correlation Analysis

A correlation heatmap was used to understand relationships between numerical features.

### Key Findings:

* Most features have **very weak correlation with salary**
* Skills like **Deep Learning and Machine Learning** showed moderate positive correlation
* `years_experience` showed **near-zero correlation**, which is unusual

👉 This indicates the dataset is more **categorical-driven** rather than numeric.

---

## 🛠️ Feature Engineering

* Converted categorical variables using encoding
* Created dummy variables for:

  * Job titles
  * Experience levels
  * Company size
  * Country

This helped the model understand non-numeric data effectively.

---

## 🤖 Model Building

We trained two models:

### 1️⃣ Linear Regression

* Achieved very high R² (~0.99)
* But likely overfitting or influenced by structured data

---

### 2️⃣ Random Forest Regressor (Final Model ✅)

* More robust and realistic
* Handles non-linear relationships well

---

## 📈 Model Evaluation

### Metrics used:

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)
* R² Score

### Final Results:

* **R² Score ≈ 0.93**
* **MAE ≈ 2448**

👉 The model explains about **93% of salary variation**

---

## 🔁 Cross-Validation

We used 5-fold cross-validation:

* Scores: ~0.93, 0.94, 0.94, 0.93, 0.93
* Mean Score: **~0.935**

### ✅ Insight:

* Model is **stable**
* No major overfitting
* Performs consistently across different data splits

---

## 🔥 Feature Importance (Key Insight)

Top important features:

1. Experience Level (Senior, Mid)
2. Job Role (ML Engineer, Data roles)
3. Company Type (MNC)

### ❗ Important Finding:

* `years_experience` had **very low importance**
* Skills like Python/SQL had minimal impact

👉 This suggests:

> Salary depends more on **role and level**, not just years or individual skills

---

## ⚡ Model Improvements

To improve performance further, we:

* Tuned Random Forest parameters:

  * Increased number of trees (`n_estimators`)
  * Controlled depth (`max_depth`)
* Removed low-importance features
* Used cross-validation for better generalization

---

## 🚀 Future Improvements

* Hyperparameter tuning using GridSearchCV
* Use advanced models like XGBoost
* Apply SHAP for deeper explainability
* Deploy model using Streamlit

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn

---

## 💯 Final Conclusion

This project shows that:

* Salary prediction is highly influenced by **experience level and job role**
* Traditional factors like years of experience may not always be strong predictors
* Random Forest provides a reliable and stable model for this problem

---

## 👨‍💻 Author

Moh Azeem
B.Tech CSE | Aspiring Data Analyst / ML Engineer
