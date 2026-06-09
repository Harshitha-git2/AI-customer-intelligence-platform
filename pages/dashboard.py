import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Customer Dashboard")

df = pd.read_csv("data/customers.csv")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", len(df))
c2.metric("Average Age", round(df["age"].mean(), 1))
c3.metric("Average Income", f"₹{int(df['income'].mean())}")
c4.metric("Churn Rate", f"{round(df['churn'].mean()*100,2)}%")

st.markdown("---")

city_counts = df["city"].value_counts().reset_index()
city_counts.columns = ["City", "Customers"]

fig = px.bar(
    city_counts,
    x="City",
    y="Customers",
    title="Customers by City"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.histogram(
    df,
    x="income",
    nbins=20,
    title="Income Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.histogram(
    df,
    x="spending_score",
    nbins=20,
    title="Spending Score Distribution"
)

st.plotly_chart(fig3, use_container_width=True)