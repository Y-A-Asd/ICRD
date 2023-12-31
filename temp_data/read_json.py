import json
from core.crudORM.insertion import Insertion
import os


CODE_DIR= os.path.dirname(os.path.abspath(__file__))


def manage_data():
    with open(f'{CODE_DIR}/data_sample.json', 'r') as file:
        data = json.load(file)
    for i in data:
        table: str = i["model"].split(".")[1]
        id = i["pk"]
        values = list(i["fields"].values())
        keys = list(i["fields"].keys())
        values.insert(0,id)
        column_data = dict(zip(["id"] + keys, values))
        yield table,column_data

