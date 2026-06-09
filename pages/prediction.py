import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.title("🤖 AI Churn Prediction")

model = joblib.load(
    "models/churn_model.pkl"
)

st.subheader("Customer Information")

income = st.number_input(
    "Annual Income",
    min_value=10000,
    max_value=300000,
    value=50000
)

spending_score = st.slider(
    "Spending Score",
    1,
    100,
    50
)

tenure = st.slider(
    "Customer Tenure (Months)",
    1,
    60,
    12
)

if st.button("Predict Churn Risk"):

    customer = pd.DataFrame(
        [[income, spending_score, tenure]],
        columns=[
            "income",
            "spending_score",
            "tenure"
        ]
    )

    prediction = model.predict(customer)[0]

    probability = model.predict_proba(customer)[0]

    churn_probability = round(
        probability[1] * 100,
        2
    )

    retention_probability = round(
        probability[0] * 100,
        2
    )

    if prediction == 1:

        st.error(
            f"⚠️ High Churn Risk ({churn_probability}%)"
        )

    else:

        st.success(
            f"✅ Customer Likely To Stay ({retention_probability}%)"
        )

    chart = pd.DataFrame({
        "Category": [
            "Retention",
            "Churn"
        ],
        "Value": [
            retention_probability,
            churn_probability
        ]
    })

    fig = px.pie(
        chart,
        names="Category",
        values="Value",
        title="Prediction Probability"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("AI Insights")

    if spending_score < 30:
        st.warning(
            "Customer spending is very low."
        )

    if tenure < 12:
        st.warning(
            "Customer has low tenure."
        )

    if income > 100000:
        st.success(
            "High-value customer."
        )