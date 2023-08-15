import pandas as pd
import json

# Open the XLSX file
xlsx_filename = 'test.xlsx'

# Read all sheets into a dictionary of dataframes
sheet_dict = pd.read_excel(xlsx_filename, sheet_name=None)

# Iterate through sheets and calculate number of rows and total row size
for sheet_name, df in sheet_dict.items():
    # num_rows = df.shape[0]
    # total_row_size = df.memory_usage(deep=True).sum()

    # print(f"Sheet: {sheet_name}")
    # print(f"Number of rows: {num_rows}")
    # print(f"Total row size: {total_row_size} bytes")
    # print("-" * 30)

    # Convert dataframe to JSON and write to a file
    json_filename = f"{sheet_name}.json"
    df.to_json(json_filename, orient='records', lines=True)
    print(f"JSON file '{json_filename}' has been created")
