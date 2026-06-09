import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.title("⚠️ Customer Churn Analytics & Prediction")

df = pd.read_csv("data/customers.csv")

model = joblib.load(
    "models/churn_model.pkl"
)

st.header("Predict Customer Churn")

col1,col2,col3 = st.columns(3)

with col1:
    income = st.number_input(
        "Income",
        10000,
        300000,
        50000
    )

with col2:
    spending = st.slider(
        "Spending Score",
        1,
        100,
        50
    )

with col3:
    tenure = st.slider(
        "Tenure",
        1,
        60,
        12
    )

if st.button("Predict"):

    input_data = pd.DataFrame(
        [[income, spending, tenure]],
        columns=[
            "income",
            "spending_score",
            "tenure"
        ]
    )

    prediction = model.predict(
        input_data
    )[0]

    prob = model.predict_proba(
        input_data
    )[0]

    churn_prob = round(
        prob[1] * 100,
        2
    )

    retain_prob = round(
        prob[0] * 100,
        2
    )

    if prediction == 1:

        st.error(
            f"⚠️ High Churn Risk : {churn_prob}%"
        )

    else:

        st.success(
            f"✅ Customer Likely To Stay : {retain_prob}%"
        )

    chart_df = pd.DataFrame({
        "Category":[
            "Retention",
            "Churn"
        ],
        "Value":[
            retain_prob,
            churn_prob
        ]
    })

    fig = px.pie(
        chart_df,
        names="Category",
        values="Value"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.header("Churn Analytics")

rate = round(
    df["churn"].mean()*100,
    2
)

st.metric(
    "Overall Churn Rate",
    f"{rate}%"
)

fig1 = px.histogram(
    df,
    x="tenure",
    color="churn",
    title="Tenure vs Churn"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

fig2 = px.scatter(
    df,
    x="income",
    y="spending_score",
    color=df["churn"].astype(str),
    title="Income vs Spending"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

risk = df[
    (df["tenure"] < 12)
    &
    (df["spending_score"] < 40)
]

st.subheader("High Risk Customers")

st.dataframe(risk)