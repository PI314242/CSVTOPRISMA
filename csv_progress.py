import os
import re
import pandas as pd
import numpy as np

def load_csvs_from_directory(directory):

    #load all csv files from the directory and analyze them

    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    dataframes = []
    
    for csv_file in csv_files:
        data = []
        day_match = re.search(r'(\d+)day', csv_file)
        order_match = re.search(r'_(\d+)\.csv', csv_file)
        day = int(day_match.group(1)) if day_match else None
        order = int(order_match.group(1)) if order_match else None

        file_path = os.path.join(directory, csv_file)
        df = pd.read_csv(file_path)
        nan_row = df.index[df.isna().all(axis=1)]  # Returns indices of fully NaN rows
        flag = 0
        for index in nan_row:
            # print(f"Row {index} in {csv_file} is fully NaN and will be dropped.")
            if index - flag > 1:
                data.append(analyze_each_table(df.iloc[flag:index]))
            flag = index + 1
        if flag < len(df):
            data.append(analyze_each_table(df.iloc[flag:]))
        
        dataframes.append({"day": day, "version": order, "data": data})
    return dataframes


def analyze_each_table(table):
    # Analyze each table to extract the table name and clean the data(remove empty rows and columns, add column names)
    first_row = table.iloc[0]
    table_name = first_row.dropna().values[0] if first_row.notna().any() else "Unknown"
    table_wo_info = table.iloc[1:]

    filtered = table_wo_info.dropna(how='all').reset_index(drop=True)

    filtered.columns = filtered.iloc[0]
    filtered = filtered.iloc[1:].reset_index(drop=True)
    filtered = filtered.dropna(axis=1, how='all')

    cols = list(filtered.columns)
    cols[0] = "sunday"
    cols[1] = "classify"
    cols[2] = "type"
    filtered.columns = cols
    return {"tableName": table_name, "data": filtered}


def execute_csv(dir):
    dataframes = load_csvs_from_directory(dir)

