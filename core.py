def run_setup():
    import JSONhandler
    filedir = JSONhandler.run_setup()
    return filedir

def importJSON(filedir): #should be in the top level program, should be run at the initialisation of the program
    import JSONhandler
    data, size = JSONhandler.importJSON(filedir)
    print("import successful")
    return data, size

def areacodes_to_csv(data):
    import parser
    parser.areacodes_to_csv(data)

def plot_single(data, size):
    while True:
        try:
            areacode = str(input("Give areacode to plot or \"q\" to quit: "))
            if areacode == ("q" or "Q"):
                break
            else:
                data_arr = collect_data(data, size, areacode)
                plot_data(data_arr, size)

        except KeyError:
            print('\033[31m' + "Error: " + '\033[0m' + "Please enter a valid areacode")

def plot_from_list(data, size):
    print('not implemented')

def plot_from_csv(data, size):
    import csv
    file = csv.reader(open('data/list.csv', 'r', encoding = 'utf-8'))
    list = []

    for row in file:
        list.append(row[0])

    print(list)

def collect_data(data, size, areacode):
    import parser
    return parser.collect_data(data, size, areacode)

def plot_data(arr, size):
    import MPLdiagrams
    print('plotter')
    MPLdiagrams.plotter(arr, size)

def main():
    try:
        filedir = run_setup()
        data, size = importJSON(filedir)

        while True:
            print('1: Write area codes to txt\n2: Plot single area\n3: Plot areas from list\n4: Plot areas from csv\nq: Quit')
            mode = input('Give the operation code: ')
            if (mode == '1'):
                areacodes_to_csv(data)
            elif mode == '2':
                plot_single(data, size)
            elif mode == '3':
                plot_from_list(data, size)
            elif mode == '4':
                plot_from_csv(data, size)
            elif mode == 'q':
                break
            else:
                print('\033[31m' + "Error: " + '\033[0m' + "Please enter a valid operation code.\n")

    except FileNotFoundError:
        print('\033[31m' + "Error: " + '\033[0m' + "Check the filename.")
    except ModuleNotFoundError as e:
        print('\033[31m' + "Error: " + '\033[0m' + str(e))

main()
