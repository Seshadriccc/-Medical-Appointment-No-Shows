# Data Cleaning and Preprocessing Task

## Overview
This repository contains the solution for Task 1 of the Data Analyst Internship: Data Cleaning and Preprocessing. The dataset used is the "Medical Appointment No Shows" dataset from Kaggle.

## Steps Performed
- Loaded the dataset (`KaggleV2-May-2016.csv`).
- Identified and handled missing values by dropping rows with missing critical columns.
- Removed duplicate rows.
- Renamed columns to lowercase with underscores (e.g., 'no-show' to 'no_show').
- Converted date columns to datetime format.
- Standardized text values (e.g., Gender to 'M'/'F', No-show to 1/0).
- Filtered ages to be between 0 and 100.
- Dropped unnecessary columns (PatientId, AppointmentID).
- Saved the cleaned dataset as `cleaned_medical_appointments.csv`.

## Files
- `data_cleaning.py`: Python script for cleaning the dataset.
- `KaggleV2-May-2016.csv`: Raw dataset (or link to Kaggle: https://www.kaggle.com/datasets/joniarroba/noshowappointments).
- `cleaned_medical_appointments.csv`: Cleaned dataset.
- Screenshots: Terminal output showing the script execution.

## How to Run
1. Place `KaggleV2-May-2016.csv` in the same directory as `data_cleaning.py`.
2. Run the script using: `python data_cleaning.py`.
3. The cleaned dataset will be saved as `cleaned_medical_appointments.csv`.