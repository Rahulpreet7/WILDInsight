import os
import pandas as pd

# Paths
RAW_PATH = "data/raw/Austin_Animal_Center_Intakes.csv"
OUTPUT_PATH = "data/processed/cleaned_intakes.csv"

def load_data(path):
    print("Loading raw intake data...")
    return pd.read_csv(path)

def standardize_columns(df):
    print("Standardizing column names...")
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def parse_datetime(df):
    print("Parsing datetime and extracting features...")
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
    df['month'] = df['datetime'].dt.month
    df['year'] = df['datetime'].dt.year
    df['season'] = df['datetime'].dt.month % 12 // 3 + 1
    df['season'] = df['season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})
    return df

def clean_categorical(df):
    print("Cleaning categorical columns...")
    df['intake_condition'] = df['intake_condition'].str.title().fillna('Unknown')
    df['intake_type'] = df['intake_type'].str.title().fillna('Unknown')
    df['animal_type'] = df['animal_type'].str.title().fillna('Unknown')
    df['found_location'] = df['found_location'].astype(str).str.strip().replace('', 'Unknown')

    # Clean additional columns
    df['name'] = df['name'].replace({'None': 'No Name', None: 'No Name', '': 'No Name'})
    df['name'] = df['name'].astype(str).str.strip()
    # Remove leading asterisks and whitespace, capitalize name
    df['name'] = df['name'].str.replace(r'^\*+', '', regex=True).str.strip().str.title()
    df['sex_upon_intake'] = df['sex_upon_intake'].astype(str).str.title().replace({'Nan': 'Unknown', '': 'Unknown'})
    df['age_upon_intake'] = df['age_upon_intake'].astype(str).str.title().replace({'Nan': 'Unknown', '': 'Unknown'})
    df['breed'] = df['breed'].astype(str).str.title().str.strip().replace({'': 'Unknown', 'Nan': 'Unknown'})
    df['color'] = df['color'].astype(str).str.title().str.replace('/', '-').str.replace(';', '-').str.replace('&', 'And').str.strip()

    return df

def save_cleaned_data(df, output_path):
    print(f"Saving cleaned data to {output_path}...")
    df.to_csv(output_path, index=False)

def main():
    df = load_data(RAW_PATH)
    df = standardize_columns(df)
    df = parse_datetime(df)
    df = clean_categorical(df)
    save_cleaned_data(df, OUTPUT_PATH)
    print("Intake data cleaning complete!")

if __name__ == "__main__":
    main()
