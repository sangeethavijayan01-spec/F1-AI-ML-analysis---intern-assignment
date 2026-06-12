# 🏎️ F1 Race Performance Analysis & Predictive Modelling

## 📌 Project Overview

This project analyzes the **Formula 1 Bahrain Grand Prix 2024 Race Session** using the FastF1 API and applies a complete data science workflow including:

- Data Collection
- Data Cleaning & Preparation
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Modelling
- Performance Anomaly Detection

The objective is to predict Formula 1 lap times and identify unusual driver performance patterns using race telemetry and timing data.

---

## 🛠 Technologies Used

- Python
- FastF1
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```text
F1-AI-ML-analysis---intern-assignment/
│
├── f1_analysis.py
├── README.md
├── .gitignore
│
└── plots/
    ├── lap_distribution.png
    ├── compound_boxplot.png
    ├── sector_comparison.png
    ├── speed_correlation.png
    ├── predicted_vs_actual.png
    ├── feature_importance.png
    └── anomaly_detection.png
```

---

## 📊 Dataset

**Source:** FastF1 Official Formula 1 Timing Data

**Session Used:**
- Bahrain Grand Prix 2024
- Race Session (R)

Data includes:

- Driver Information
- Lap Times
- Sector Times
- Tyre Compounds
- Tyre Life
- Speed Traps
- Team Information

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

- Selected relevant race-performance columns
- Converted lap and sector times to seconds
- Removed missing values
- Removed outlier laps (>120 seconds)
- Reset dataframe index after cleaning

---

## 📈 Exploratory Data Analysis

### 1. Lap Time Distribution
- Histogram of lap times
- Mean and median indicators

### 2. Tyre Compound Performance
- Boxplot comparison of:
  - Soft
  - Medium
  - Hard

### 3. Sector Analysis
- Average Sector 1, Sector 2 and Sector 3 times by driver

### 4. Speed Correlation
- Relationship between Speed Trap speed and Lap Time
- Pearson Correlation Analysis

---

## ⚙️ Feature Engineering

Engineered features include:

### Sector Balance

```python
SectorBalance = Sector1Time - Sector3Time
```

### Tyre Age Categories

- Fresh (1–10 laps)
- Used (11–25 laps)
- Old (26+ laps)

### Encoding

- One-Hot Encoding for tyre compounds
- One-Hot Encoding for tyre age buckets
- Driver encoding for model training

---

## 🤖 Machine Learning Model

### Model Used

```python
RandomForestRegressor
```

### Train/Test Split

```python
80% Training
20% Testing
```

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🚨 Anomaly Detection

A statistical anomaly detection approach was implemented.

A lap is flagged as anomalous when:

```python
LapTime > DriverMedian + (2 × DriverStdDev)
```

This helps identify:

- Driver mistakes
- Tyre degradation effects
- Traffic impacts
- Potential car issues

---

## 📷 Generated Visualizations

| Visualization | Description |
|--------------|-------------|
| lap_distribution.png | Lap time distribution |
| compound_boxplot.png | Tyre compound comparison |
| sector_comparison.png | Sector performance analysis |
| speed_correlation.png | Speed vs Lap Time |
| predicted_vs_actual.png | Model prediction accuracy |
| feature_importance.png | Top predictive features |
| anomaly_detection.png | Driver anomaly detection |

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/sangeethavijayan01-spec/F1-AI-ML-analysis---intern-assignment.git
```

Install dependencies:

```bash
pip install fastf1 pandas numpy scikit-learn matplotlib seaborn
```

---

## ▶️ Run the Project

```bash
python f1_analysis.py
```

Generated plots will be saved automatically inside:

```text
plots/
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- End-to-End Data Science Workflow
- Sports Analytics
- Data Visualization
- Feature Engineering
- Machine Learning Regression
- Anomaly Detection
- GitHub Project Management

---

## 👩‍💻 Author

**Sangeetha V**

AI/ML Engineering Intern Assignment  
DataCore Analytics – Data Science Track (2026)
