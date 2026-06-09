# 🤖 AI-Driven Customer Intelligence Platform

An AI-powered customer analytics platform built using Streamlit, Machine Learning, Pandas, Scikit-Learn, and Plotly.

This project helps businesses analyze customer behavior, predict churn risk, segment customers, generate insights, and improve customer retention strategies.

---

# 🚀 Features

## 📊 Customer Dashboard

- Customer overview
- KPI metrics
- Income distribution
- Spending score analysis
- Customer demographics

## 🎯 Customer Segmentation

- K-Means clustering
- Customer grouping
- Premium customers identification
- Segment-wise analysis
- Interactive visualizations

## ⚠️ Churn Analytics

- Churn distribution
- Risk customer identification
- Income vs churn analysis
- Spending behavior analysis
- Retention insights

## 🤖 Churn Prediction

Predict customer churn probability using:

- Income
- Spending Score
- Customer Tenure

Machine Learning Model:

- Random Forest Classifier

## 🎁 Recommendation Engine

- Similar customer discovery
- Product recommendations
- Customer behavior analysis

## 📈 Executive Insights Dashboard

- Business KPIs
- Customer trends
- Revenue insights
- Strategic analytics
- Interactive reports

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Plotly
- Faker
- Joblib
- Matplotlib
- Seaborn

---

# 📂 Project Structure

```text
AI_Customer_Intelligence_Platform
│
├── app.py
├── generate_dataset.py
├── train_models.py
├── requirements.txt
│
├── data/
│   └── customers.csv
│
├── models/
│   └── churn_model.pkl
│
├── pages/
│   ├── dashboard.py
│   ├── segmentation.py
│   ├── churn.py
│   ├── prediction.py
│   ├── recommendations.py
│   └── insights_dashboard.py
│
├── assets/
│   ├── logos.png
│   └── styles.css
│
└── .streamlit/
    └── config.toml
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/AI_Customer_Intelligence_Platform.git

cd AI_Customer_Intelligence_Platform
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Or

```bash
pip install streamlit pandas numpy plotly scikit-learn matplotlib seaborn faker joblib
```

---

# 📊 Generate Dataset

```bash
python generate_dataset.py
```

Output:

```text
Dataset Created Successfully
```

---

# 🧠 Train Machine Learning Model

```bash
python train_models.py
```

Output:

```text
Model Saved Successfully
```

---

# ▶️ Run Application

```bash
python -m streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

# 📈 Machine Learning Workflow

## Dataset Generation

Synthetic customer data is generated using:

- Faker
- Randomized business metrics

Attributes include:

- Customer ID
- Name
- Age
- Gender
- City
- Income
- Spending Score
- Tenure
- Churn Status

---

## Customer Segmentation

Algorithm:

```text
K-Means Clustering
```

Used Features:

- Income
- Spending Score

Purpose:

- Identify customer groups
- Support targeted marketing

---

## Churn Prediction

Algorithm:

```text
Random Forest Classifier
```

Features:

- Income
- Spending Score
- Tenure

Output:

- Churn Probability
- Retention Probability
- Risk Category

---

# 📸 Screens

### Home Dashboard

- KPI Cards
- AI Metrics
- Customer Overview

### Segmentation

- Cluster Visualization
- Customer Segments

### Churn Analytics

- Risk Analysis
- Churn Charts

### Prediction

- AI Churn Prediction Form

### Recommendations

- Product Recommendations
- Similar Customers

### Executive Dashboard

- Strategic Business Insights

---

# 🎯 Project Objectives

- Understand customer behavior
- Predict customer churn
- Improve customer retention
- Generate business intelligence
- Support data-driven decisions

---

# 🔮 Future Enhancements

- Customer Lifetime Value Prediction
- RFM Analysis
- Deep Learning Models
- Real Database Integration
- Authentication System
- PDF Report Export
- Email Alerts
- Real-Time Analytics

---

# 👨‍💻 Author

Developed as an AI-based Customer Analytics and Intelligence Platform project using Machine Learning and Data Visualization.

---

# 📄 License

This project is intended for educational, research, and portfolio purposes.
