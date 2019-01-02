def run_setup():
    from JSONhandler import run_setup
    data_dir, export_dir, report_dir = run_setup()
    return data_dir, export_dir, report_dir

def importJSON(filedir): #should be in the top level program, should be run at the initialisation of the program
    from JSONhandler import importJSON
    data, size = importJSON(filedir)
    return data, size

def areacodes_to_csv(data):
    from parser import areacodes_to_csv
    areacodes_to_csv(data)

def plot_data(areacode, arr, size, mode, filedir):
    from MPLdiagrams import plotter
    plotter(areacode, arr, size, mode, filedir)

def collect_data(data, size, areacode):
    from parser import collect_data
    return collect_data(data, size, areacode)

def plot_single(data, size, filedir):
    try:
        while True:
            areacode = str(input("Give areacode to plot or \"q\" to quit: "))
            if areacode == ("q" or "Q"):
                break
            else:
                data_arr = collect_data(data, size, areacode)
                plot_data(areacode, data_arr, size, 'visual', filedir)

    except KeyError:
        print('\033[31m' + "Error: " + '\033[0m' + "Please enter a valid areacode")

def plot_from_list(data, size, list, filedir):
    for areacode in list:
        data_arr = collect_data(data, size, areacode)
        plot_data(areacode, data_arr, size, 'svg', filedir)

def plot_from_csv(data, size, filedir):
    from csv import reader as csv_reader
    file = csv_reader(open('data/list.csv', 'r', encoding = 'utf-8'))
    list = []

    for row in file:
        list.append(row[0])
    plot_from_list(data, size, list, filedir)

def merge_data(data, data_dir, report_dir, size):
    from fix_data import merge
    merge(data, data_dir, report_dir, size)

def fix_data(data, data_dir, size):
    from fix_data import fix
    fix(data, data_dir, size)

def main():
    try:
        import os
        data_dir, export_dir, report_dir = run_setup()
        data, size = importJSON(data_dir)
        export_dir = str(export_dir + '2018/')
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        list = []

        while True:
            print('1: Write area codes to txt\n2: Plot areas\n3: Fix data\nq: Quit')
            mode = input('Give the operation code: ')
            if (mode == '1'):
                areacodes_to_csv(data)
            elif mode == '2':
                print('1: Plot single area\n2: Plot areas from list\n3: Plot areas from csv\nq: Quit')
                mode = input('Give the operation code: ')
                if mode == '1':
                    plot_single(data, size, export_dir)
                elif mode == '2':
                    plot_from_list(data, size, export_dir)
                elif mode == '3':
                    plot_from_csv(data, size, export_dir)

            elif mode == '3':
                print('1: Fix values individually\n2: Merge two areacodes\nq: Quit')
                mode = input('Give the operation code: ')
                if mode == '1':
                    fix_data(data, data_dir, size)
                elif mode == '2':
                    merge_data(data, data_dir, report_dir, size)

            elif mode == 'q':
                break
            else:
                print('\033[31m' + "Error: " + '\033[0m' + "Please enter a valid operation code.\n")

    except FileNotFoundError:
        print('\033[31m' + "Error: " + '\033[0m' + "Check the filename.")
    except ModuleNotFoundError as e:
        print('\033[31m' + "Error: " + '\033[0m' + str(e))

main()
