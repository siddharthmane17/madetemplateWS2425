import pandas as pd
from sqlalchemy import create_engine
import os
import sqlite3
import requests
from io import StringIO
import shutil
import openpyxl

# Function to download the datasets
def download_csv_files():
    dataset_path = os.path.join(os.getcwd(), "data")
    os.makedirs(dataset_path, exist_ok=True)

    # Download Solar Footprints Dataset
    solar_url = 'https://cecgis-caenergy.opendata.arcgis.com/api/download/v1/items/9398e39a0424434b9e95ccf8e8938807/csv?layers=0'
    solar_csv_path = os.path.join(dataset_path, "solar_data.csv")
    solar_response = requests.get(solar_url)
    with open(solar_csv_path, "wb") as f:
        f.write(solar_response.content)
    
    # Download Electric Vehicle Dataset
    electric_url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
    electric_csv_path = os.path.join(dataset_path, "electric_vehicle_data.csv")
    electric_response = requests.get(electric_url)
    with open(electric_csv_path, "wb") as f:
        f.write(electric_response.content)

    # Read CSV files into DataFrames
    solar_df = pd.read_csv(solar_csv_path)
    electric_df = pd.read_csv(electric_csv_path)
    
    return solar_df, electric_df

# Function to clean the Solar Footprints Data
def clean_solar_data(dataframe):
    solar_cleaned_df = dataframe
    solar_cleaned_df.dropna(inplace=True)
    solar_cleaned_df.columns = [col.strip().replace(" ", "_") for col in solar_cleaned_df.columns]
    return solar_cleaned_df

# Function to save the Solar Footprints Data to SQLite and Excel
def save_solar_data(dataframe):
    solar_cleaned_df = dataframe
    # Connect to SQLite database
    sql_file_path = os.path.join(os.getcwd(), "data", "Solar.sqlite")
    conn = sqlite3.connect(sql_file_path)
    # Save to Excel
    excel_file_path = os.path.join(os.getcwd(), "data", "solar_data.xlsx")
    solar_cleaned_df.to_excel(excel_file_path, index=False)
    # Save to SQLite
    solar_cleaned_df.to_sql('SolarFootprints', conn, index=False, if_exists='replace')
    conn.close()

# Function to clean the Electric Vehicle Data
def clean_electric_data(dataframe):
    electric_cleaned_df = dataframe
    electric_cleaned_df.dropna(inplace=True)
    electric_cleaned_df.columns = [col.strip().replace(" ", "_") for col in electric_cleaned_df.columns]
    return electric_cleaned_df

# Function to save the Electric Vehicle Data to SQLite and Excel
def save_electric_data(dataframe):
    electric_cleaned_df = dataframe
    # Connect to SQLite database
    sql_file_path = os.path.join(os.getcwd(), "data", "Electric.sqlite")
    conn = sqlite3.connect(sql_file_path)
    # Save to Excel
    excel_file_path = os.path.join(os.getcwd(), "data", "electric_vehicle_data.xlsx")
    electric_cleaned_df.to_excel(excel_file_path, index=False)
    # Save to SQLite
    electric_cleaned_df.to_sql('ElectricVehicles', conn, index=False, if_exists='replace')
    conn.close()

# Main data pipeline function
def data_pipeline():
    print("Downloading datasets...")
    solar_df, electric_df = download_csv_files()
    print("Download complete")

    # Step 2: Clean Solar Footprints dataset and save it
    print("Cleaning Solar Footprints data...")
    solar_cleaned_df = clean_solar_data(solar_df)
    print("Saving Solar Footprints data to SQLite and Excel...")
    save_solar_data(solar_cleaned_df)
    print("Solar Footprints data saved successfully")

    # Step 3: Clean Electric Vehicle dataset and save it
    print("Cleaning Electric Vehicle data...")
    electric_cleaned_df = clean_electric_data(electric_df)
    print("Saving Electric Vehicle data to SQLite and Excel...")
    save_electric_data(electric_cleaned_df)
    print("Electric Vehicle data saved successfully")
    
    print("All tasks completed successfully :)")

if __name__ == "__main__":
    data_pipeline()
