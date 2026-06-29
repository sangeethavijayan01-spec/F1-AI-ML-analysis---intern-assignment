# 🏎️ F1 AI/ML Race Performance Analysis

## Live Demo
 
https://sangeethavijayan01-spec.github.io/F1-AI-ML-analysis---intern-assignment/

---

## GitHub Repository

📂 Source Code:

https://github.com/sangeethavijayan01-spec/F1-AI-ML-analysis---intern-assignment

---

## Project Overview

This project performs a complete Data Science and Machine Learning workflow using official Formula 1 race data from the 2024 Bahrain Grand Prix.

The objective is to analyze race performance, understand factors affecting lap times, build a predictive model, and identify unusual driver performance using anomaly detection techniques.

---

## Technologies Used

- FastF1
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit

---

## Project Workflow

### 1. Data Collection

- Connected to official Formula 1 timing data using FastF1
- Loaded Bahrain Grand Prix 2024 Race Session
- Extracted lap-by-lap performance data

### 2. Data Cleaning

- Removed invalid laps
- Filtered missing values
- Converted timing columns into numerical seconds
- Removed outlier lap records

### 3. Exploratory Data Analysis

Performed:

- Lap Time Distribution Analysis
- Tyre Compound Performance Comparison
- Sector Performance Analysis
- Speed Trap Correlation Analysis

### 4. Feature Engineering

Created new machine learning features including:

- Sector Balance
- Tyre Age Categories
- Compound Encoding
- Driver Encoding

### 5. Machine Learning

Model Used:

**Random Forest Regressor**

Goal:

- Predict Formula 1 lap times using race telemetry and performance features

Evaluation:

- Predicted vs Actual Comparison
- Feature Importance Analysis

### 6. Anomaly Detection

Detected unusual laps by comparing:

- Driver Median Lap Time
- Driver Standard Deviation

Laps exceeding expected performance thresholds were flagged as anomalies.

---

# Dashboard Features

The Streamlit Dashboard includes:

### 📊 Exploratory Data Analysis

- Lap Time Distribution
- Compound Performance Analysis
- Sector Comparison
- Speed Correlation Analysis

### 🤖 Machine Learning

- Predicted vs Actual Lap Times
- Feature Importance Visualization

### 🚨 Anomaly Detection

- Driver Performance Monitoring
- Detection of Unusual Laps
- Performance Deviation Analysis

---

## Generated Visualizations

The project automatically generates:

- lap_distribution.png
- compound_boxplot.png
- sector_comparison.png
- speed_correlation.png
- predicted_vs_actual.png
- feature_importance.png
- anomaly_detection.png

---

## Project Structure

```text
F1-AI-ML-analysis---intern-assignment/
│
├── app.py
├── f1_analysis.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── plots/
│   ├── lap_distribution.png
│   ├── compound_boxplot.png
│   ├── sector_comparison.png
│   ├── speed_correlation.png
│   ├── predicted_vs_actual.png
│   ├── feature_importance.png
│   └── anomaly_detection.png
│
└── f1_cache/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sangeethavijayan01-spec/F1-AI-ML-analysis---intern-assignment.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Analysis Script

```bash
python f1_analysis.py
```

---

## Run Dashboard

```bash
streamlit run app.py
```

---

## Key Learning Outcomes

- Data Collection from APIs
- Data Cleaning & Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning Modelling
- Model Evaluation
- Statistical Anomaly Detection
- Interactive Dashboard Development

---

## Author

**Sangeetha V**

AI/ML Engineering Internship Project

Formula 1 Race Performance Analytics

2024 Bahrain Grand Prix Analysis
