import json
import os
import pandas as pd

SAMPLE_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sample_data_files')

if __name__ == "__main__":

    # Reading a json file and converting it into a dataframe

    json_file_path = os.path.join(SAMPLE_DATA_DIR, 'employee_dataset_json.json')
    with open(json_file_path, 'r') as employee_json_file:
        employee_data = json.load(employee_json_file)

    print(employee_data['employees'])
    print(type(employee_data['employees']))

    employee_data_df = pd.json_normalize(employee_data['employees'])
    print(employee_data_df)

    # Concatenating the address row values in the dataframe

    # employee_data_df['full_address'] = employee_data_df.apply(
    #     lambda row: row['address.street'] + ', ' + row['address.city'] + ', ' + row['address.state'] +
    #                 ', Zip Code:' + row['address.zip_code'], axis=1
    # )
    employee_data_df['full_address'] = (
            employee_data_df['address.street'] + ', ' + employee_data_df['address.city'] + ', ' +
            employee_data_df['address.state'] + ', Zip Code:' + employee_data_df['address.zip_code']
    )
    print(employee_data_df)

    # Dropping columns from a dataframe

    employee_data_df = employee_data_df.drop(
        columns=['address.street', 'address.city', 'address.state', 'address.zip_code']
    )
    print(employee_data_df)

    # Sorting the dataframe using a particular column

    employee_data_df = employee_data_df.sort_values(by='salary', ascending=False)
    print(employee_data_df)

    # Grouping the dataframe by a specific column and aggregate

    employee_data_df = employee_data_df.groupby(by='department').agg(
        employees=('id', 'count'),
        total_salary=('salary', 'sum'),
    )
    print(employee_data_df)
