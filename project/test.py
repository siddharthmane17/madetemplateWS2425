import pandas as pd
import os
import sqlite3

# Function to test if data exists in a given table
def test_file(sql_file_path, table_name):
    # Connect to SQLite database
    conn = sqlite3.connect(sql_file_path)

    # Query to select all rows from the table
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)

    if len(df) > 0:
        print(f"Data exists in the '{table_name}' table in the SQL file.")
    else:
        print(f"No data found in the '{table_name}' table.")

    # Close the connection
    conn.close()

# Function to check for null values in the table
def check_null(sql_file_path, table_name):
    # Connect to SQLite database
    conn = sqlite3.connect(sql_file_path)

    # Query to select all rows from the table
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)

    if df.isnull().any().any():
        print(f"The '{table_name}' table contains null values.")
    else:
        print(f"The '{table_name}' table does not contain null values.")

    # Close the connection
    conn.close()

# Main test function
def test_dataset():
    # Step 1: Test SolarFootprints dataset
    print("Testing SolarFootprints dataset...")
    sql_file_path_solar = os.path.join(os.getcwd(), "data", "Solar.sqlite")
    table_name_solar = "SolarFootprints"
    test_file(sql_file_path_solar, table_name_solar)
    print("Test 1.1 completed for SolarFootprints dataset.")

    print("Checking for null values in SolarFootprints dataset...")
    check_null(sql_file_path_solar, table_name_solar)
    print("Test 1.2 completed for SolarFootprints dataset.")

    # Step 2: Test ElectricVehicles dataset
    print("Testing ElectricVehicles dataset...")
    sql_file_path_electric = os.path.join(os.getcwd(), "data", "Electric.sqlite")
    table_name_electric = "ElectricVehicles"
    test_file(sql_file_path_electric, table_name_electric)
    print("Test 2.1 completed for ElectricVehicles dataset.")

    print("Checking for null values in ElectricVehicles dataset...")
    check_null(sql_file_path_electric, table_name_electric)
    print("Test 2.2 completed for ElectricVehicles dataset.")
    
    print("All tests are completed and are running successfully!)")

if __name__ == "__main__":
    test_dataset()
