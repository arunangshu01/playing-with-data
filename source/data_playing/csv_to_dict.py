from csv import DictReader
import os

SAMPLE_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sample_data_files')

if __name__ == "__main__":

    # Reading a csv file and converting it into a dictionary

    csv_file_path = os.path.join(SAMPLE_DATA_DIR, 'employee_dataset_csv.csv')
    with open(csv_file_path, 'r') as employee_csv_file:
        employee_data_dict = DictReader(employee_csv_file)
        employee_data_dict_list = list(employee_data_dict)
    print(employee_data_dict_list)
