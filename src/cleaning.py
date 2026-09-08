def clean_data(df):
    print("Starting Data Cleaning...")
    numeric_missing = [
        "Age",
        "Height_cm",
        "Weight_kg",
        "Blood_Glucose",
        "HbA1c",
        "Exercise_Hours_Per_Week",
        "Daily_Walking_Minutes",
        "Sleep_Hours",
        "Total_Cholesterol",
        "HDL",
        "LDL",
        "Triglycerides",
    ]
    df[numeric_missing] = df[numeric_missing].fillna(df[numeric_missing].median()
                                                     )
    categorical_missing = [
        "Physical_Activity_Level",
        "Medication_Adherence",
    ]
    for col in categorical_missing:
     df[col] = df[col].fillna(df[col].mode()[0]

                               ) 
    return(df)

