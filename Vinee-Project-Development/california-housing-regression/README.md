# California Housing Price Prediction – Regression Models

This project implements an end-to-end regression pipeline to predict median house prices using the California Housing dataset.  
The focus is on building multiple regression models, applying proper feature scaling, and evaluating model performance using standard regression metrics.

---

##  Dataset
- Source: `sklearn.datasets.fetch_california_housing`
- Total records: 20,640
- Features: 8 numerical features
- Target variable: **Median House Value (MedHouseVal)**

---

## ⚙️ Project Workflow

1. Data ingestion using sklearn built-in dataset
2. Train-test split
3. Feature scaling using StandardScaler
4. Model training
5. Model evaluation using RMSE and R²
6. Logging and exception handling throughout the pipeline

---

## Models Implemented

- Linear Regression
- Ridge Regression
- ElasticNet Regression

---

## Model Evaluation Metrics

| Model              | RMSE   | R² Score |
|--------------------|--------|----------|
| Linear Regression  | 0.7456 | 0.5758   |
| Ridge Regression   | 0.7456 | 0.5758   |
| ElasticNet         | 0.7974 | 0.5148   |

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- NumPy
- Custom logging & exception handling


