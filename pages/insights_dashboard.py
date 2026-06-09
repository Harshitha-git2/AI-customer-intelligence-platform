import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Executive Insights")

df = pd.read_csv(
    "data/customers.csv"
)

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Customers",
    len(df)
)

c2.metric(
    "Avg Income",
    f"₹{int(df['income'].mean())}"
)

c3.metric(
    "Avg Spending",
    round(
        df["spending_score"].mean(),
        2
    )
)

c4.metric(
    "Churn Rate",
    f"{round(df['churn'].mean()*100,2)}%"
)

fig1 = px.histogram(
    df,
    x="income",
    title="Income Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

fig2 = px.histogram(
    df,
    x="spending_score",
    title="Spending Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

city = (
    df["city"]
    .value_counts()
    .reset_index()
)

city.columns = [
    "City",
    "Count"
]

fig3 = px.bar(
    city,
    x="City",
    y="Count",
    title="Customers by City"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

fig4 = px.scatter(
    df,
    x="income",
    y="spending_score",
    color="city",
    title="Income vs Spending by City"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.subheader(
    "Top Customers"
)

top = df.sort_values(
    "income",
    ascending=False
)

st.dataframe(
    top.head(20)
)