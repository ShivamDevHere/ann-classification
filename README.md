# Artificial Neural Network-Based Customer Churn Prediction

An Artificial Neural Network (ANN) based machine learning project that predicts whether a bank customer is likely to leave the bank using customer demographics, account information, and banking activity.

## Project Overview

Customer churn prediction helps banks identify customers who may leave their services and take proactive steps to improve customer retention.

This project uses an ANN classification model trained on customer banking data to predict customer churn.

## Dataset

The dataset contains customer information and account attributes.

**Features include:**
- CreditScore
- Geography
- Gender
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary

**Target:** `Exited`
- `0` — Customer stays
- `1` — Customer leaves

`RowNumber`, `CustomerId`, and `Surname` are identification-related columns and are excluded from model training.

## Tech Stack

- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- TensorFlow & Keras
- Streamlit

## Workflow

1. Data loading and exploratory data analysis (EDA)
2. Data cleaning and preprocessing
3. Feature engineering
4. One-Hot Encoding for categorical features
5. Feature standardization
6. Train-test split
7. ANN model development and training
8. Model evaluation
9. Web application deployment

## Model

The project uses an Artificial Neural Network for binary classification.

The network learns patterns in customer data to estimate whether a customer is likely to leave the bank.

**Output classes:**
- `0` — Retained customer
- `1` — Churned customer

## Evaluation Metrics

## Model Performance

The ANN model was trained for **10 epochs** out of the planned 100 epochs.

| Metric | Training Result |
|---|---:|
| Training Accuracy | 86.48% |
| Validation Accuracy | 85.85% |
| Validation Loss | 0.3536 |

The model achieved **85.85% validation accuracy**, demonstrating its ability to predict customer churn on unseen validation data.

## Project Structure

```text
ANN-Customer-Churn/
├── assets
├── models/
│   ├── label_encoder_gender.pkl
│   ├── models.h5
│   ├── onehot_encoder_geo.pkl
│   └── scaler.pkl
├── 01-experiments.ipynb
├── 02-predictions.ipynb
├── README.md
└── requirements.txt
```

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/ShivamDevHere/ann-customer-churn-prediction.git
   cd ann-customer-churn-prediction
   ```

2. Create and activate a virtual environment.

   ```bash
   py -3.11 -m venv venv
   source venv/Scripts/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application: `Under Work`

   ```bash
   streamlit run app.py
   ```

## Live Demo

**Live Application:** [https://ann-customer-churn-prediction-app.streamlit.app/]

## Author

**Shivam Srivastava**

- GitHub: [ShivamDevHere](https://github.com/Shivamdevhere)
- Portfolio: [Visit Portfolio](https://portfolio-ruby-one-66.vercel.app/)

---

*Built to explore deep learning and apply artificial neural networks to a real-world customer retention problem.*
