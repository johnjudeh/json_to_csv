#!/Users/john/.pyenv/versions/json_to_csv/bin/python
"""
json_to_csv is a simple command line tool to convert json files to a csv output.

The program reads the json file into a pandas dataframe, normalising any structured data that is
nested more than a single level. This results in a flat CSV file.
"""

import argparse
import pandas as pd
import json

ARGNAME_JSON_FILE = 'json_file'
ARGNAME_CSV_FILE = 'csv_file'

def json_file_to_df(filepath):
    with open(filepath) as f:
        file_content = json.load(f)
    return pd.json_normalize(file_content)

def df_to_csv(df, output_filepath):
    df.to_csv(output_filepath, index=None, header=True)

def json_to_csv(input_path, output_path):
    df = json_file_to_df(input_path)
    df_to_csv(df, output_path)

def create_arg_parser():
    parser = argparse.ArgumentParser(description='Convert json file to csv.')
    parser.add_argument(ARGNAME_JSON_FILE, type=str, help='A path to the input json file')
    parser.add_argument(ARGNAME_CSV_FILE, type=str, help='A path to the output csv file')
    return parser

if __name__ == '__main__':
    parser = create_arg_parser()
    args_dict = vars(parser.parse_args())
    json_to_csv(args_dict[ARGNAME_JSON_FILE], args_dict[ARGNAME_CSV_FILE])
    print(f'Created csv file called {args_dict[ARGNAME_CSV_FILE]}')
