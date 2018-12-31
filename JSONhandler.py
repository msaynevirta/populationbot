from json import load, JSONDecoder

def run_setup():
    data = load(open("setup.json","r", encoding='utf-8'))
    data_dir = str(data["constants"]['data_dir'])
    export_dir = str(data["constants"]['export_dir'])

    return data_dir, export_dir

def importJSON(filedir):
    data = load(open(filedir,"r", encoding='utf-8'))

    size = data["dataset"]["dimension"]["size"]

    return data, size
