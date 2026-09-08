import pandas as pd
import numpy as np
from cleaning import clean_data
from analysis import dataset_overview ,data_quality_report,risk_distribution,patient_analysis,health_factor_analysis,correlation_analysis

df = pd.read_csv("data/diabetes_risk_prediction_dataset.csv")
df = clean_data(df)



print("=" * 60)
print("        DIABETES RISK DATA ANALYZER")
print("=" * 60)

print(f"\nDataset loaded successfully!")
print(f"Records : {len(df):,}")
print(f"Features : {len(df.columns)}")


while True:
 print("\n1. Dataset Overview")
 print("\n2. Data Quality Report")
 print("\n3. Risk Distribution")
 print("\n4. Patient Analysis")
 print("\n5. Health Factor Analysis")
 print("\n6. Correlation Analysis")
 print("\n7. Exit")

 choice = int(input("Enter your choice: "))

 if choice == 1:
    dataset_overview(df)
 elif choice == 2:
    data_quality_report(df)
 elif choice == 3:
    risk_distribution(df)
 elif choice == 4:
    patient_analysis(df)
 elif choice == 5:
    health_factor_analysis(df)
 elif choice == 6:
    correlation_analysis(df)
 elif choice == 7:
    print("Exiting..")
    break

