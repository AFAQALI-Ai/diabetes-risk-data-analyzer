# Diabetes Risk Data Analyzer

A command-line tool for exploring and analyzing a diabetes risk dataset using pandas.

## Version

V1.0

## About the Project

This is a menu-driven CLI application that loads a diabetes risk dataset, cleans it, and lets you run different kinds of analysis on it — from a quick overview of the data to looking up a single patient's records. I built it mainly to practice working with real, messy tabular data in pandas: handling missing values, grouping, correlations, and structuring a small multi-file Python project instead of one big script.

It's not a medical or diagnostic tool. The risk scores and labels come straight from the dataset, not from any model built here.

## Dataset

The script expects a CSV at `data/diabetes_risk_prediction_dataset.csv`. Each row is a patient record with:

- **Identifiers / demographics** — `Patient_ID`, `Age`, `Gender`, `Country`
- **Health measurements** — `Height_cm`, `Weight_kg`, `BMI`, `Waist_Circumference_cm`, `Blood_Glucose`, `HbA1c`, `Fasting_Blood_Sugar`, `Insulin_Level`, `Blood_Pressure_Systolic`, `Blood_Pressure_Diastolic`, `Total_Cholesterol`, `HDL`, `LDL`, `Triglycerides`
- **Lifestyle factors** — `Physical_Activity_Level`, `Exercise_Hours_Per_Week`, `Daily_Walking_Minutes`, `Sleep_Hours`, `Daily_Water_Intake_L`, `Medication_Adherence`
- **Target columns** — `Diabetes_Risk`, `Diabetes_Risk_Score`

The dataset itself isn't bundled with this repo — add your own CSV with matching column names under `data/`.

## Features

The app runs as a loop with a numbered menu:

1. **Dataset Overview** — shape, column names, data types, and a preview of the first and last rows
2. **Data Quality Report** — record and feature counts, total missing values, duplicate rows
3. **Risk Distribution** — counts of patients per `Diabetes_Risk` category
4. **Patient Analysis** — look up one patient by ID and see their basic info, health measurements, and risk info
5. **Health Factor Analysis** — average `Diabetes_Risk_Score` grouped by `Physical_Activity_Level`
6. **Correlation Analysis** — correlation of key health and lifestyle columns against `Diabetes_Risk_Score`
7. **Exit**

## Data Cleaning

Before anything else runs, `clean_data()` in `cleaning.py` handles missing values:

- Numeric columns (`Age`, `Height_cm`, `Weight_kg`, `Blood_Glucose`, `HbA1c`, `Exercise_Hours_Per_Week`, `Daily_Walking_Minutes`, `Sleep_Hours`, `Total_Cholesterol`, `HDL`, `LDL`, `Triglycerides`) are filled with their column **median**
- Categorical columns (`Physical_Activity_Level`, `Medication_Adherence`) are filled with their column **mode**

This runs once when the dataset is loaded in `main.py`, so every analysis function works on already-cleaned data.

## Analysis

Each function in `analysis.py` handles one part of the menu:

- `dataset_overview()` — prints shape, columns, dtypes, and head/tail of the DataFrame
- `data_quality_report()` — summarizes size, missing values, and duplicates
- `risk_distribution()` — value counts for `Diabetes_Risk`
- `patient_analysis()` — prompts for a `Patient_ID` and prints that patient's info in three grouped tables
- `health_factor_analysis()` — groups by activity level and averages the risk score
- `correlation_analysis()` — builds a correlation matrix over the numeric health/lifestyle columns and sorts by correlation with `Diabetes_Risk_Score`

## Technologies Used

- Python 3
- pandas
- NumPy

## Project Structure

```
diabetes-risk-analyzer/
├── main.py              # Entry point, menu loop
├── cleaning.py           # clean_data()
├── analysis.py            # All analysis functions
├── data/
│   └── diabetes_risk_prediction_dataset.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

1. Clone or download this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Place your dataset at `data/diabetes_risk_prediction_dataset.csv`
4. Run the app:
   ```
   python main.py
   ```
5. Pick an option (1–7) from the menu

## Sample Output

```
============================================================
        DIABETES RISK DATA ANALYZER
============================================================

Dataset loaded successfully!
Records : 5,000
Features : 24

1. Dataset Overview
2. Data Quality Report
3. Risk Distribution
4. Patient Analysis
5. Health Factor Analysis
6. Correlation Analysis
7. Exit
Enter your choice: 3

------------------------------------------------------------
                 RISK DISTRIBUTION
------------------------------------------------------------

[ RISK LEVEL COUNTS ]
Low       2450
Moderate  1680
High       870
Name: Diabetes_Risk, dtype: int64
```

(Numbers above are illustrative — actual output depends on the dataset you load.)

## Future Improvements

Being honest about where this project stands right now — these are things I haven't learned yet, not just nice-to-haves:

- Data visualization
- More statistical analysis
- SQL integration
- Machine learning
