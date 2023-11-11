import json
from core.crudORM.insertion import Insertion

def manage_data():
    with open('/home/flatlife/PycharmProjects/ICRD/temp_data/data_sample.json', 'r') as file:
        data = json.load(file)
    for i in data:
        table: str = i["model"].split(".")[1]
        id = i["pk"]
        values = list(i["fields"].values())
        keys = list(i["fields"].keys())
        values.insert(0,id)
        column_data = dict(zip(["id"] + keys, values))
        yield table,column_data
