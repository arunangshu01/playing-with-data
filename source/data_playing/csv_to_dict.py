from csv import DictReader
import os

if __name__ == "__main__":

    # Reading a csv file and converting it into a dictionary

    csv_file_path = os.path.join('../sample_data_files', 'employee_data_csv.csv')
    with open(csv_file_path, 'r') as employee_csv_file:
        employee_data_dict = DictReader(employee_csv_file)
        employee_data_dict_list = list(employee_data_dict)
    print(employee_data_dict_list)
