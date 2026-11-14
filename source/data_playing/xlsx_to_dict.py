import pandas as pd
import os

SAMPLE_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sample_data_files')

if __name__ == "__main__":

    # Reading a xlsx file and converting it into a dictionary

    xlsx_file_path = os.path.join(SAMPLE_DATA_DIR, 'employee_dataset_xlsx.xlsx')
    employee_data_df = pd.read_excel(xlsx_file_path)
    employee_data_dict_list = employee_data_df.to_dict('records')

    print(employee_data_dict_list)
