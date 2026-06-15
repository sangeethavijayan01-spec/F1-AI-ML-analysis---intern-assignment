import streamlit as st

st.set_page_config(
    page_title="F1 AI/ML Analytics Dashboard",
    page_icon="🏎️",
    layout="wide"
)

# ==========================
# HEADER
# ==========================

st.title("🏎️ Formula 1 AI/ML Analytics Dashboard")
st.subheader("Bahrain Grand Prix 2024")

# Dashboard Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Drivers", "20")

with col2:
    st.metric("Race", "Bahrain GP")

with col3:
    st.metric("Season", "2024")

with col4:
    st.metric("ML Model", "Random Forest")

st.success(
    "✅ Complete Formula 1 Data Science Pipeline Successfully Implemented"
)

st.markdown("---")

# ==========================
# PROJECT OVERVIEW
# ==========================

st.markdown("""
## 📋 Project Overview

This project analyzes official Formula 1 Bahrain Grand Prix 2024 race data using modern
Data Science and Machine Learning techniques.

### Technologies Used

- FastF1
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit

### Project Workflow

✔ Data Collection

✔ Data Cleaning & Preparation

✔ Exploratory Data Analysis

✔ Feature Engineering

✔ Random Forest Regression

✔ Feature Importance Analysis

✔ Anomaly Detection

### Objective

Predict Formula 1 lap times and identify unusual driver performance patterns
using machine learning models and statistical analysis.
""")

st.markdown("---")

# ==========================
# TABS
# ==========================

tab1, tab2, tab3 = st.tabs(
    ["📊 Exploratory Data Analysis",
     "🤖 Machine Learning",
     "🚨 Anomaly Detection"]
)

# ==========================
# EDA
# ==========================

with tab1:

    st.header("📊 Exploratory Data Analysis")

    st.subheader("Lap Time Distribution")

    st.image(
        "plots/lap_distribution.png",
        use_container_width=True
    )

    st.info(
        "This histogram shows the distribution of lap times across all drivers. "
        "The mean and median indicators help understand overall race pace consistency."
    )

    st.subheader("Tyre Compound Performance")

    st.image(
        "plots/compound_boxplot.png",
        use_container_width=True
    )

    st.info(
        "Comparison of Soft, Medium and Hard tyre compounds. "
        "Lower lap times indicate better performance."
    )

    st.subheader("Sector Performance Analysis")

    st.image(
        "plots/sector_comparison.png",
        use_container_width=True
    )

    st.info(
        "Average Sector 1, Sector 2 and Sector 3 times for each driver. "
        "This highlights where drivers gain or lose time."
    )

    st.subheader("Speed Trap Correlation")

    st.image(
        "plots/speed_correlation.png",
        use_container_width=True
    )

    st.info(
        "Relationship between top speed and overall lap time. "
        "The regression line indicates the correlation trend."
    )

# ==========================
# MACHINE LEARNING
# ==========================

with tab2:

    st.header("🤖 Machine Learning Model")

    st.success(
        "Random Forest Regressor trained to predict Formula 1 lap times."
    )

    st.subheader("Predicted vs Actual Lap Times")

    st.image(
        "plots/predicted_vs_actual.png",
        use_container_width=True
    )

    st.info(
        "Points closer to the diagonal reference line indicate more accurate predictions."
    )

    st.subheader("Feature Importance Analysis")

    st.image(
        "plots/feature_importance.png",
        use_container_width=True
    )

    st.info(
        "This chart identifies which variables contribute most to lap time prediction."
    )

    st.markdown("""
### Key Insight

The Random Forest model learns performance patterns from:

- Tyre Life
- Speed Trap Speed
- Sector Balance
- Lap Number
- Tyre Compound

These variables significantly influence lap time performance.
""")

# ==========================
# ANOMALY DETECTION
# ==========================

with tab3:

    st.header("🚨 Driver Anomaly Detection")

    st.image(
        "plots/anomaly_detection.png",
        use_container_width=True
    )

    st.warning(
        "Red ✕ markers indicate laps that deviate significantly from the driver's normal performance."
    )

    st.markdown("""
### Detection Method

A lap is classified as anomalous when:

**Lap Time > Driver Median + (2 × Driver Standard Deviation)**

### Possible Causes

- 🛞 Tyre degradation
- ⚠ Driver mistakes
- 🔧 Mechanical issues
- 🚦 Traffic interference
- 🛑 Pit stop related delays

This helps identify unusual race events and performance drops.
""")

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.caption(
    "🏎️ AI/ML Engineering Internship Project | Formula 1 Race Analytics | Bahrain GP 2024"
)