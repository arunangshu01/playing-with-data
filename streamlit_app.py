import json
import os

import pandas as pd
import streamlit as st

SAMPLE_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'source', 'sample_data_files')


@st.cache_data
def load_csv():
    return pd.read_csv(os.path.join(SAMPLE_DATA_DIR, 'employee_dataset_csv.csv'))


@st.cache_data
def load_json():
    with open(os.path.join(SAMPLE_DATA_DIR, 'employee_dataset_json.json'), 'r') as employee_json_file:
        return json.load(employee_json_file)


@st.cache_data
def load_xlsx():
    return pd.read_excel(os.path.join(SAMPLE_DATA_DIR, 'employee_dataset_xlsx.xlsx'))


DATASETS = {
    'CSV': {
        'script': 'csv_to_dataframe.py',
        'load': load_csv,
        'load_code': "pd.read_csv('employee_dataset_csv.csv')",
        'group_by': ['City', 'First_Name'],
        'steps': [
            ('Concatenate columns', "df['Full_Name'] = df['First_Name'] + ' ' + df['Last_Name']",
             lambda df: df.assign(Full_Name=df['First_Name'] + ' ' + df['Last_Name'])),
            ('Drop columns', "df = df.drop(columns=['First_Name', 'Last_Name'])",
             lambda df: df.drop(columns=['First_Name', 'Last_Name'])),
            ('Reindex columns', "df = df.reindex(columns=['ID', 'Full_Name', 'Age', 'City', 'Salary', 'Joining_Date'])",
             lambda df: df.reindex(columns=['ID', 'Full_Name', 'Age', 'City', 'Salary', 'Joining_Date'])),
            ('Sort', "df = df.sort_values(by=['Age', 'Salary'], ascending=True)",
             lambda df: df.sort_values(by=['Age', 'Salary'], ascending=True)),
            ('Group & aggregate',
             "df = df.groupby(by='City').agg(\n    Employees=('ID', 'count'),\n    Average_Age=('Age', 'mean'),\n"
             "    Total_Salary=('Salary', 'sum'),\n)",
             lambda df: df.groupby(by='City').agg(
                 Employees=('ID', 'count'), Average_Age=('Age', 'mean'), Total_Salary=('Salary', 'sum'))),
        ],
    },
    'JSON': {
        'script': 'json_to_dataframe.py',
        'load': lambda: pd.json_normalize(load_json()['employees']),
        'load_code': "pd.json_normalize(json.load(f)['employees'])",
        'group_by': ['department', 'address.city', 'address.state'],
        'steps': [
            ('Concatenate columns',
             "df['full_address'] = (\n    df['address.street'] + ', ' + df['address.city'] + ', ' +\n"
             "    df['address.state'] + ', Zip Code:' + df['address.zip_code']\n)",
             lambda df: df.assign(full_address=df['address.street'] + ', ' + df['address.city'] + ', ' +
                                  df['address.state'] + ', Zip Code:' + df['address.zip_code'])),
            ('Drop columns',
             "df = df.drop(columns=['address.street', 'address.city', 'address.state', 'address.zip_code'])",
             lambda df: df.drop(columns=['address.street', 'address.city', 'address.state', 'address.zip_code'])),
            ('Sort', "df = df.sort_values(by='salary', ascending=False)",
             lambda df: df.sort_values(by='salary', ascending=False)),
            ('Group & aggregate',
             "df = df.groupby(by='department').agg(\n    employees=('id', 'count'),\n"
             "    total_salary=('salary', 'sum'),\n)",
             lambda df: df.groupby(by='department').agg(employees=('id', 'count'), total_salary=('salary', 'sum'))),
        ],
    },
    'Excel': {
        'script': 'xlsx_to_dataframe.py',
        'load': load_xlsx,
        'load_code': "pd.read_excel('employee_dataset_xlsx.xlsx')",
        'group_by': ['Department'],
        'steps': [
            ('Concatenate columns', "df['Joined_String'] = df['Name'] + '_' + df['Department']",
             lambda df: df.assign(Joined_String=df['Name'] + '_' + df['Department'])),
            ('Drop columns', "df = df.drop(columns=['Name'])",
             lambda df: df.drop(columns=['Name'])),
            ('Reindex columns',
             "df = df.reindex(columns=['Employee_ID', 'Joined_String', 'Department', 'Salary',\n"
             "                         'Years_Of_Experience', 'Joining_Date'])",
             lambda df: df.reindex(columns=['Employee_ID', 'Joined_String', 'Department', 'Salary',
                                            'Years_Of_Experience', 'Joining_Date'])),
            ('Sort', "df = df.sort_values(by=['Salary', 'Years_Of_Experience'], ascending=True)",
             lambda df: df.sort_values(by=['Salary', 'Years_Of_Experience'], ascending=True)),
            ('Group & aggregate',
             "df = df.groupby(by='Department').agg(\n    Employees=('Employee_ID', 'count'),\n"
             "    Total_Salary=('Salary', 'sum'),\n    Average_Experience=('Years_Of_Experience', 'mean'),\n)",
             lambda df: df.groupby(by='Department').agg(
                 Employees=('Employee_ID', 'count'), Total_Salary=('Salary', 'sum'),
                 Average_Experience=('Years_Of_Experience', 'mean'))),
        ],
    },
}

AGGREGATIONS = {
    'sum': 'Total',
    'mean': 'Average',
    'median': 'Median',
    'min': 'Minimum',
    'max': 'Maximum',
    'count': 'Number of employees',
}


def column_label(column):
    return column.replace('address.', '').replace('_', ' ').capitalize()


st.set_page_config(page_title='Playing with data', layout='wide')
st.title('Playing with data')
st.caption('Loading, transforming and aggregating employee data from CSV, JSON and Excel files with pandas.')

source = st.sidebar.radio('Data source', list(DATASETS))
dataset = DATASETS[source]
st.sidebar.markdown(f"Script: `source/data_playing/{dataset['script']}`")

df = dataset['load']()

pipeline_tab, raw_tab, explore_tab = st.tabs(['Step-by-step pipeline', 'As dictionary', 'Explore'])

with pipeline_tab:
    st.subheader('0. Load')
    st.code(dataset['load_code'], language='python')
    st.caption(f'{len(df):,} rows x {len(df.columns)} columns')
    st.dataframe(df, width='stretch', height=250, alt=f'Raw {source} employee data')

    result = df
    for i, (title, code, step) in enumerate(dataset['steps'], start=1):
        result = step(result)
        st.subheader(f'{i}. {title}')
        st.code(code, language='python')
        st.caption(f'{len(result):,} rows x {len(result.columns)} columns')
        st.dataframe(result, width='stretch', height=250 if len(result) > 6 else 'content',
                     alt=f'Employee data after step {i}: {title.lower()}')

with raw_tab:
    if source == 'JSON':
        st.json(load_json())
    else:
        st.caption("First 20 records via `df.to_dict('records')`")
        st.json(json.loads(df.head(20).to_json(orient='records', date_format='iso')))

with explore_tab:
    numeric_columns = [column for column in df.select_dtypes(include='number').columns
                       if not column.lower().endswith('id')]
    st.caption('Pick a category, a number and how to summarise it to build your own pandas aggregation.')
    left, middle, right = st.columns(3)
    group_by = left.selectbox('Group by', dataset['group_by'], format_func=column_label, key=f'{source}_group_by')
    value = middle.selectbox('Value', numeric_columns, format_func=column_label, key=f'{source}_value',
                             index=next((i for i, c in enumerate(numeric_columns) if c.lower() == 'salary'), 0))
    aggregation = right.selectbox('Aggregation', list(AGGREGATIONS), format_func=AGGREGATIONS.get,
                                  key=f'{source}_aggregation')

    grouped = df.groupby(group_by)[value].agg(aggregation).sort_values(ascending=False)
    description = f'{AGGREGATIONS[aggregation].lower()} {column_label(value).lower()} by {column_label(group_by).lower()}'
    st.code(f"df.groupby('{group_by}')['{value}'].agg('{aggregation}')", language='python')
    chart_column, table_column = st.columns([2, 1])
    chart_column.bar_chart(grouped, alt=f'Bar chart of {description}')
    table_column.dataframe(grouped, width='stretch', alt=f'Table of {description}')
