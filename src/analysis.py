
# Dataset Overview:

def dataset_overview(df):

    print("\n" + "-" * 60)
    print("                 DATASET OVERVIEW")
    print("-" * 60)

    print("\n[ DATASET SHAPE ]")
    print(df.shape)

    print("\n[ COLUMN NAMES ]")
    print(df.columns.tolist())

    print("\n[ DATA TYPES ]")
    print(df.dtypes)

    print("\n[ FIRST 5 ROWS ]")
    print(df.head())

    print("\n[ LAST 5 ROWS ]")
    print(df.tail())


# Data Quality Report:

def data_quality_report(df):

    print("\n" + "-" * 60)
    print("                 DATA QUALITY REPORT")
    print("-" * 60)

    print("\n[ DATASET SIZE ]")
    print(f"Total Records    : {len(df):,}")
    print(f"Total Features   : {len(df.columns)}")

    print("\n[ MISSING VALUES ]")
    total_missing = df.isnull().sum().sum()
    print(f"Missing Values   : {total_missing:,}")

    print("\n[ DUPLICATE ROWS ]")
    duplicate_rows = df.duplicated().sum()
    print(f"Duplicate Rows   : {duplicate_rows:,}")


# Risk Distribution:

def risk_distribution(df):

    print("\n" + "-" * 60)
    print("                 RISK DISTRIBUTION")
    print("-" * 60)

    print("\n[ RISK LEVEL COUNTS ]")
    print(df["Diabetes_Risk"].value_counts())

# Patient Analysis:

def patient_analysis(df):

    patient_id = int(input("Enter Patient Id: "))

    patient = df[df["Patient_ID"] == patient_id]

    if patient.empty:
        print("No Patient Found")

    else:
        print("\n" + "-" * 60)
        print("                 PATIENT ANALYSIS")
        print("-" * 60)

        basic_info = patient[
            ["Patient_ID", "Age", "Gender", "Country"]
        ]

        health_info = patient[
            ["BMI", "Blood_Glucose", "HbA1c"]
        ]

        risk_info = patient[
            ["Diabetes_Risk", "Diabetes_Risk_Score"]
        ]

        print("\n[ BASIC INFORMATION ]")
        print(basic_info.to_string(index=False))

        print("\n[ HEALTH MEASUREMENTS ]")
        print(health_info.to_string(index=False))

        print("\n[ RISK INFORMATION ]")
        print(risk_info.to_string(index=False))

# Health Factor Analysis:

def health_factor_analysis(df):

    print("\n" + "-" * 60)
    print("                 HEALTH FACTOR ANALYSIS")
    print("-"*60)
    print("\n[ ACTIVITY LEVEL vs RISK SCORE ]")
    result = df.groupby("Physical_Activity_Level")["Diabetes_Risk_Score"].mean()
    print(result)

# Correlation Analysis:

def correlation_analysis(df):

    print("\n" + "-" * 60)
    print("                 CORRELATION ANALYSIS")
    print("-" * 60)

    print("\n[ CORRELATION MATRIX ]")
    columns = [
    "Age",
    "BMI",
    "Waist_Circumference_cm",
    "Blood_Glucose",
    "HbA1c",
    "Fasting_Blood_Sugar",
    "Insulin_Level",
    "Blood_Pressure_Systolic",
    "Blood_Pressure_Diastolic",
    "Total_Cholesterol",
    "HDL",
    "LDL",
    "Triglycerides",
    "Exercise_Hours_Per_Week",
    "Daily_Walking_Minutes",
    "Sleep_Hours",
    "Daily_Water_Intake_L",
    "Diabetes_Risk_Score"
                           ]

    print(df[columns].corr()["Diabetes_Risk_Score"].sort_values(ascending=False))