import json
import pandas as pd
import os
import sys

def read_json():
    with open('source_class.json', 'r') as json_dict:
        content = json.load(json_dict)
    return content

def display_user_names(json_file:dict , output_file = list()) -> list:
    val_content = json_file['results']
    for a in val_content:
        b = a['replies']
        for c in b:
            user_name = c['user']['display_name']
            output_file.append(user_name)

    return output_file


if __name__=='__main__':
    content = read_json()
    print(display_user_names(content))