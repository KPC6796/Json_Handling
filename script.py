import pandas as pd
import json
import csv
import sys
import os
import pathlib

def json_to_csv(json_file_path : str, csv_file_nm) -> None:
    with open(json_file_path) as json_file:
        data = json.load(json_file)
        headers = data[0].keys()

        with open(csv_file_nm, 'w') as csv_file_local:
            writer = csv.writer(csv_file_local)
            writer.writerow(headers)

            for record in data:
                rec = (value for value in record.values())
                writer.writerow(rec)

if __name__=='__main__':
    try:
        json_file_path = sys.argv[1]
        csv_file_nm = sys.argv[2]

    except IndexError:
        sys.exit("Two arguments required, one json file path and other csv file name")

    with pathlib.Path(json_file_path) as json_file_global:
        if json_file_global.is_file():
            json_to_csv(json_file_path, csv_file_nm)

            df = pd.read_csv(csv_file_nm)
            print(df.head())

        else:
            print(f"Did not find {json_file_path}")
