import pandas as pd
import os

if __name__ == "__main__":

    # Reading a xlsx file and converting it into a dataframe

    xlsx_file_path = os.path.join('../sample_data_files', 'employee_dataset_xlsx.xlsx')
    employee_data_df = pd.read_excel(xlsx_file_path)

    print(employee_data_df)

    # Concatenating the string row values in the dataframe

    employee_data_df['Joined_String'] = (employee_data_df['Name'] + '_' + employee_data_df['Department'])
    print(employee_data_df)

    # Dropping columns from a dataframe

    employee_data_df = employee_data_df.drop(
        columns=['Name']
    )
    print(employee_data_df)

    # Reindexing the concatenated column in the dataframe

    employee_data_df = employee_data_df.reindex(columns=['Employee_ID', 'Joined_String', 'Department', 'Salary', 'Years_Of_Experience', 'Joining_Date'])
    print(employee_data_df)

    # Sorting the dataframe using a particular column

    employee_data_df = employee_data_df.sort_values(by=['Salary', 'Years_Of_Experience'], ascending=True)
    print(employee_data_df)

    # Grouping the dataframe by a specific column and aggregate

    employee_data_df['Joining_Date'] = employee_data_df['Joining_Date'].astype(dtype=str)
    employee_data_df = employee_data_df.groupby(by='Department').sum()
    print(employee_data_df)
