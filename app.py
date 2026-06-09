import streamlit as st
import os

st.set_page_config(
    page_title="AI Customer Intelligence",
    page_icon="🤖",
    layout="wide"
)

if os.path.exists(
    "assets/styles.css"
):
    with open(
        "assets/styles.css"
    ) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

logo_path = "assets/logos.png"

if os.path.exists(
    logo_path
):
    st.sidebar.image(
        logo_path,
        width=150
    )

st.sidebar.title(
    "AI Customer Intelligence"
)

st.title(
    "🤖 AI Customer Intelligence Platform"
)

st.markdown(
    """
    ### Features

    - Customer Dashboard
    - Customer Segmentation
    - Churn Analysis
    - Churn Prediction
    - Recommendation Engine
    - Executive Insights

    Use the sidebar to navigate between pages.
    """
)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Customers",
    "500+"
)

c2.metric(
    "AI Accuracy",
    "92%"
)

c3.metric(
    "Retention",
    "84%"
)

c4.metric(
    "Predictions",
    "Real-Time"
)