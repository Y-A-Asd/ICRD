import json
from core.crudORM.insertion import Insertion

def manage_data(conn):
    insertion = Insertion(conn)
    with open("data_sample.json", "r") as file:
        data = json.load(file)
    for i in data:
        table = i["model"].split(".")[1]
        id = i["pk"]
        values = list(i["fields"].values())
        keys = list(i["fields"].keys())
        values.insert(0,id)
        column_data = dict(zip(["id"] + keys, values))
        insertion.insert_data(table_name=table,column_data=column_data)
