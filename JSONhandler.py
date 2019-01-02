from json import load, JSONDecoder, JSONDecodeError

def run_setup():
    data = load(open('setup.json', 'r', encoding='utf-8'))
    data_dir = str(data['constants']['data_dir'])
    export_dir = str(data['constants']['export_dir'])
    report_dir = str(data['constants']['report_dir'])

    return data_dir, export_dir, report_dir

def importJSON(filedir):
    try:
        data = load(open(filedir,'r', encoding='utf-8'))

        size = data['dataset']['dimension']['size']

        return data, size
    except JSONDecodeError:
        print('\033[31m' + "Error: " + '\033[0m' + "Failed to read the data file")
        return False
