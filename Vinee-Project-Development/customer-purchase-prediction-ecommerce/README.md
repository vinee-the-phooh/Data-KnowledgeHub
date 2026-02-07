# Customer Purchase Prediction – E-commerce

This project implements an end-to-end machine learning pipeline to predict whether a customer will purchase a product after viewing it, using an e-commerce dataset.

## Dataset
- Source: Kaggle (E-commerce Product Purchase)
- Records: 1,000
- Features: Demographic, behavioural, and product-related attributes
- Target variable: **purchase** (0 = No, 1 = Yes)


##  Project Workflow

1. Data ingestion from CSV
2. Data cleaning and ID column removal
3. Train-test split with stratification
4. Feature engineering:
   - One-hot encoding for categorical variables
   - Standard scaling for numerical features
5. Model training using Logistic Regression
6. Model evaluation using ROC-AUC and confusion matrix
7. Model persistence and metric reporting


## Model Used
- Logistic Regression (with class imbalance handling)



## Model Performance

- **ROC-AUC:** 0.997  
- **Evaluation methods:**
  - ROC curve

The ROC curve shows excellent class separation, indicating strong predictive performance.



## Tech Stack
- Python
- Pandas
- Scikit-learn
- NumPy
- Matplotlib
- Custom logging & exception handling
