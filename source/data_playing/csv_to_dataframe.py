import pandas as pd
import os

if __name__ == "__main__":

    # Reading a csv file and converting it into a dataframe

    csv_file_path = os.path.join('../sample_data_files', 'employee_dataset_csv.csv')
    with open(csv_file_path, 'r') as employee_csv_file:
        employee_data_df = pd.read_csv(employee_csv_file)

    print(employee_data_df)

    # Concatenating the name row values in the dataframe

    employee_data_df['Full_Name'] = (employee_data_df['First_Name'] + ' ' + employee_data_df['Last_Name'])
    print(employee_data_df)

    # Dropping columns from a dataframe

    employee_data_df = employee_data_df.drop(
        columns=['First_Name', 'Last_Name']
    )
    print(employee_data_df)

    # Reindexing the concatenated column in the dataframe

    employee_data_df = employee_data_df.reindex(columns=['ID', 'Full_Name', 'Age', 'City', 'Salary', 'Joining_Date'])
    print(employee_data_df)

    # Sorting the dataframe using a particular column

    employee_data_df = employee_data_df.sort_values(by=['Age', 'Salary'], ascending=True)
    print(employee_data_df)

    # Grouping the dataframe by a specific column and aggregate

    employee_data_df = employee_data_df.groupby(by='City').sum()
    print(employee_data_df)
