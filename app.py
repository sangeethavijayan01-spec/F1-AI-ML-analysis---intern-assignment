import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="F1 AI/ML Analytics Dashboard",
    page_icon="🏎️",
    layout="wide"
)

# Load race data
laps = pd.read_csv("race_data.csv")

# ==========================
# HEADER
# ==========================

st.title("🏎️ Formula 1 AI/ML Analytics Dashboard")
st.subheader("Bahrain Grand Prix 2024")

# Lap Selector
current_lap = st.slider(
    "🏁 Select Race Lap",
    1,
    int(laps["LapNumber"].max()),
    1
)

lap_data = laps[laps["LapNumber"] <= current_lap]

# Dashboard Metrics
# Dashboard Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Current Lap", current_lap)

with col2:
    st.metric(
        "Drivers",
        lap_data["Driver"].nunique()
    )

with col3:
    st.metric(
        "Fastest Speed",
        f"{lap_data['SpeedST'].max():.1f} km/h"
    )

with col4:
    st.metric(
        "Laps Analysed",
        len(lap_data)
    )

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

    st.subheader("Tyre Compound Performance")

    st.image(
        "plots/compound_boxplot.png",
        use_container_width=True
    )

    st.subheader("Sector Performance Analysis")

    st.image(
        "plots/sector_comparison.png",
        use_container_width=True
    )

    st.subheader("Speed Trap Correlation")

    fig = px.scatter(
        lap_data,
        x="SpeedST",
        y="LapTime",
        color="Compound",
        title=f"Speed vs Lap Time (Up to Lap {current_lap})",
        hover_data=["Driver"]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
        "Relationship between top speed and overall lap time. "
        "The chart updates automatically when the lap slider changes."
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