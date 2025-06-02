import pandas as pd
import numpy as np
import os

possible_paths = [
    'KaggleV2-May-2016.csv',  
    '../KaggleV2-May-2016.csv',  
    'data/KaggleV2-May-2016.csv',  
]

file_path = None
for path in possible_paths:
    if os.path.exists(path):
        file_path = path
        break

if not file_path:
    print("Error: File 'KaggleV2-May-2016.csv' not found in any of the specified paths.")
    print("Current directory contents:", os.listdir('.'))
    print("Contents of 'data' subdirectory:", os.listdir('data') if os.path.exists('data') else "Directory 'data' not found")
    print("Parent directory contents:", os.listdir('..'))
    print("Please place 'KaggleV2-May-2016.csv' in the 'archive' directory.")
    exit(1)

print(f"Loading dataset from {file_path} ...")
df = pd.read_csv(file_path)
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())
df = df.dropna(subset=['AppointmentDay', 'No-show'])
if df['Age'].isnull().sum() > 0:
    df['Age'].fillna(df['Age'].median(), inplace=True)
print("\nMissing Values After Handling:")
print(df.isnull().sum())

initial_rows = df.shape[0]
df = df.drop_duplicates()
print(f"\nRemoved {initial_rows - df.shape[0]} duplicate rows.")
print("Shape after removing duplicates:", df.shape)

df.columns = df.columns.str.lower().str.replace('-', '_')
df.rename(columns={
    'patientid': 'patient_id',
    'appointmentid': 'appointment_id',
    'scheduledday': 'scheduled_day',
    'appointmentday': 'appointment_day',
    'neighbourhood': 'neighborhood',
    'hipertension': 'hypertension',
    'handcap': 'handicap',
    'sms_received': 'sms_received',
    'no_show': 'no_show'
}, inplace=True)
print("\nRenamed Columns:")
print(df.columns.tolist())

df['scheduled_day'] = pd.to_datetime(df['scheduled_day'], errors='coerce')
df['appointment_day'] = pd.to_datetime(df['appointment_day'], errors='coerce')
df['age'] = df['age'].astype(int, errors='ignore')
df = df[(df['age'] >= 0) & (df['age'] <= 100)]
print("\nData Types After Conversion:")
print(df.dtypes)

df['gender'] = df['gender'].str.upper().str.strip()
df['no_show'] = df['no_show'].map({'Yes': 1, 'No': 0})
df['neighborhood'] = df['neighborhood'].str.upper().str.strip()

df = df.drop(['patient_id', 'appointment_id'], axis=1, errors='ignore')
print("\nColumns After Dropping Unnecessary Ones:")
print(df.columns.tolist())

output_path = 'cleaned_medical_appointments.csv'
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset saved to {output_path}")
print("Final Shape:", df.shape)

print("\nSummary of Changes:")
print("- Loaded dataset with shape:", df.shape)
print("- Handled missing values by dropping rows with missing 'appointment_day' or 'no_show'.")
print("- Removed duplicate rows.")
print("- Renamed columns to lowercase with underscores (e.g., 'no-show' to 'no_show').")
print("- Converted 'scheduled_day' and 'appointment_day' to datetime.")
print("- Standardized 'gender' (M/F) and 'neighborhood' (uppercase).")
print("- Converted 'no_show' to binary (1 for Yes, 0 for No).")
print("- Dropped unnecessary columns: 'patient_id', 'appointment_id'.")
print("- Filtered ages to be between 0 and 100.")
print("- Saved cleaned dataset as 'cleaned_medical_appointments.csv'.")
print("- Final shape:", df.shape)