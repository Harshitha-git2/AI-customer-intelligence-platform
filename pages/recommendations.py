import streamlit as st
import pandas as pd

st.title("🎁 Customer Recommendations")

df = pd.read_csv(
    "data/customers.csv"
)

customer_id = st.selectbox(
    "Select Customer",
    df["customer_id"]
)

customer = df[
    df["customer_id"] == customer_id
]

st.dataframe(customer)

income = customer["income"].values[0]

similar = df[
    df["income"].between(
        income - 15000,
        income + 15000
    )
]

st.subheader(
    "Similar Customers"
)

st.dataframe(
    similar.head(15)
)

st.subheader(
    "Recommended Products"
)

recommendations = [
    "Laptop",
    "Smartphone",
    "Smart Watch",
    "Headphones",
    "Tablet"
]

for item in recommendations:
    st.success(item)