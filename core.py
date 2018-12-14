def run_setup():
    import JSONhandler
    filedir = JSONhandler.run_setup()
    return filedir

def importJSON(filedir): #should be in the top level program, should be run at the initialisation of the program
    import JSONhandler
    data, size = JSONhandler.importJSON(filedir)
    print("import successful")
    return data, size

def areacodes_to_txt(data):
    import parser
    parser.areacodes_to_txt(data)

def collect_data(data, size, areacode):
    import parser
    return parser.collect_data(data, size, areacode)

def plot_data(arr, size):
    import MPLdiagrams
    print("plotter")
    MPLdiagrams.plotter(arr, size)

def main():
    try:
        filedir = run_setup()
        data, size = importJSON(filedir)
        while True:
            try:
                print("1: Write area codes to txt\n2: Plot data\n3: Quit")
                mode = int(input("Give the operation number: "))
                if (mode == 1):
                    areacodes_to_txt(data)
                elif mode == 2:
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
                elif mode == 3:
                    break
            except ValueError:
                print('\033[31m' + "Error: " + '\033[0m' + "Please enter the number as a positive int.")
    except FileNotFoundError:
        print('\033[31m' + "Error: " + '\033[0m' + "Check the filename.")
    except ModuleNotFoundError as e:
        print('\033[31m' + "Error:" + '\033[0m' + str(e))
main()
