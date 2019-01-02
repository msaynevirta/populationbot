def collect_data(data, size, areacode):
    from parser import collect_data
    return collect_data(data, size, areacode)

def write_new_arr(data, size, areacode, list_to_write):
    from parser import write_data
    write_data(data, size, areacode, list_to_write)

def merge(data, data_dir, report_dir, size):
    val_list = []
  
    areacode1 = input('Please enter the first areacode: ')
    areacode2 = input('Please enter the second areacode: ')
    
    lab1 = data["dataset"]["dimension"]["Alue"]["category"]["label"][areacode1] #find the labels for the given areacodes
    lab2 = data["dataset"]["dimension"]["Alue"]["category"]["label"][areacode2]
    print('Merging {:s} to {:s}'.format(lab1, lab2))
    
    report_file = str(report_dir + 'merges.txt') #write a log entry
    with open(report_file, 'a') as f:
        f.write('Merged {:s} ({:s}) to {:s} ({:s})\n'.format(lab1, areacode1, lab2, areacode2))
    
    data_arr1 = collect_data(data, size, areacode1)
    data_arr2 = collect_data(data, size, areacode2)

    #merge fuction (replace nulls)

    write_new_arr(data, size, areacode1, arr_to_write) #replace the original data associated with the first areacode with the merged data

def fix(data, filename, size):
    areacode = input('Please enter areacode: ')
    
    raw_list = collect_data(data, size, areacode)

    print(raw_list)
    val_list = raw_list[1]

    print('Current data, please enter the fixed data as a list')
    print(val_list)

    val_list = [int(x) for x in input().split(', ')]

    write_data(data, size, areacode, val_list)

