import streamlit as st

st.set_page_config(
    page_title="F1 AI/ML Analysis",
    page_icon="🏎️",
    layout="wide"
)

st.title("🏎️ Formula 1 Race Performance Analysis")
st.subheader("Bahrain Grand Prix 2024")

st.markdown("""
## Project Overview

This project uses official Formula 1 race data from the Bahrain Grand Prix 2024
to perform a complete AI/ML workflow:

- Data Collection using FastF1
- Data Cleaning and Preparation
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Random Forest Regression
- Anomaly Detection

The goal is to predict lap times and identify unusual driver performance.
""")

tab1, tab2, tab3 = st.tabs([
    "📊 Exploratory Data Analysis",
    "🤖 Machine Learning",
    "🚨 Anomaly Detection"
])

with tab1:

    st.header("Lap Time Distribution")

    st.image(
        "plots/lap_distribution.png",
        caption="Distribution of lap times across all drivers. Gold line indicates mean lap time and teal line indicates median lap time."
    )

    st.header("Tyre Compound Performance")

    st.image(
        "plots/compound_boxplot.png",
        caption="Comparison of lap times across Soft, Medium and Hard tyre compounds."
    )

    st.header("Sector Analysis")

    st.image(
        "plots/sector_comparison.png",
        caption="Average Sector 1, Sector 2 and Sector 3 times for each driver."
    )

    st.header("Speed Correlation")

    st.image(
        "plots/speed_correlation.png",
        caption="Relationship between Speed Trap speed and overall lap time."
    )

with tab2:

    st.header("Random Forest Lap Time Prediction")

    st.image(
        "plots/predicted_vs_actual.png",
        caption="Comparison between actual lap times and model predictions. Points closer to the reference line indicate better predictions."
    )

    st.header("Feature Importance")

    st.image(
        "plots/feature_importance.png",
        caption="Top features influencing lap time prediction according to the Random Forest model."
    )

with tab3:

    st.header("Anomaly Detection")

    st.image(
        "plots/anomaly_detection.png",
        caption="Red X markers represent laps identified as anomalous compared to each driver's normal performance."
    )

st.markdown("---")

st.success(
    "AI/ML Internship Project - Formula 1 Race Performance Analysis"
)

st.markdown(
    "Developed using FastF1, Pandas, Scikit-Learn, Matplotlib and Seaborn."
)