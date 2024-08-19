import json
import os


if __name__ == "__main__":

    # Reading a json file and converting it into a dictionary

    json_file_path = os.path.join('../sample_data_files', 'employee_dataset_json.json')
    with open(json_file_path, 'r') as employee_json_file:
        employee_data = json.load(employee_json_file)

    print(employee_data)
