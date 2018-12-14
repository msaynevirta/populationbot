import json

def run_setup():
    data = json.load(open("setup.json","r", encoding='utf-8'))
    filedir = str(data["constants"]['filedir'])
    return filedir

def importJSON(filedir):
    data = json.load(open(filedir,"r", encoding='utf-8'))

    size = data["dataset"]["dimension"]["size"]

    return data, size
