import streamlit as st
import pandas as pd

from sklearn.cluster import KMeans

import plotly.express as px

st.title("🎯 Customer Segmentation")

df = pd.read_csv(
    "data/customers.csv"
)

clusters = st.slider(
    "Select Number of Segments",
    2,
    6,
    4
)

X = df[
    [
        "income",
        "spending_score"
    ]
]

kmeans = KMeans(
    n_clusters=clusters,
    random_state=42,
    n_init=10
)

df["Segment"] = kmeans.fit_predict(X)

st.metric(
    "Total Segments",
    clusters
)

fig = px.scatter(
    df,
    x="income",
    y="spending_score",
    color=df["Segment"].astype(str),
    hover_data=["city"]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

segment_count = (
    df["Segment"]
    .value_counts()
)

fig2 = px.pie(
    values=segment_count.values,
    names=segment_count.index
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

segment_summary = (
    df.groupby("Segment")
    [
        [
            "income",
            "spending_score"
        ]
    ]
    .mean()
)

st.dataframe(
    segment_summary
)

selected = st.selectbox(
    "View Segment",
    sorted(df["Segment"].unique())
)

st.dataframe(
    df[
        df["Segment"] == selected
    ]
)