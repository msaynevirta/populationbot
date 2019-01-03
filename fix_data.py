def collect_data(data, size, areacode):
    from parser import collect_data
    return collect_data(data, size, areacode)

def write_new_arr(data, size, filename, areacode, list_to_write):
    from parser import write_data
    write_data(data, size, filename, areacode, list_to_write)

def write_merge_report(data, report_dir, areacode1, areacode2, was_successful)
    report_file = str(report_dir + 'merges.txt') #write a log entry

    lab1 = data["dataset"]["dimension"]["Alue"]["category"]["label"][areacode1] #find the labels for the given areacodes
    lab2 = data["dataset"]["dimension"]["Alue"]["category"]["label"][areacode2]
    print('Merging {:s} to {:s}'.format(lab1, lab2))
    
    with open(report_file, 'a') as f:
        if was_successful == True: #if merge is successful
            f.write('Merged {:s} ({:s}) to {:s} ({:s})\n'.format(lab1, areacode1, lab2, areacode2))
        else: # if merge fails (write_new_arr returns False)
            f.write('ERROR: Merging {:s} ({:s}) to {:s} ({:s}) failed\n'.format(lab1, areacode1, lab2, areacode2))

def merge(data, data_dir, report_dir, size):
    val_list = []
  
    areacode1 = input('Please enter the first areacode: ')
    areacode2 = input('Please enter the second areacode: ')
       
    raw_arr1 = collect_data(data, size, areacode1)
    raw_arr2 = collect_data(data, size, areacode2)
    
    data_arr1 = raw_arr1[1]
    data_arr2 = raw_arr2[1]

    i = 0
    print(data_arr1)
    for val in  data_arr1:
        if val == None:
            data_arr1[i] = data_arr2[i]
        i += 1
 
    if input('Continue?') == 'q':
        return False
    else:
        w = write_new_arr(data, size, data_dir, areacode1, data_arr1) #replace the original data associated with the first areacode with the merged data
        write_merge_report(data, report_dir, areacode1, areacode2, w)

def fix(data, filename, size):
    areacode = input('Please enter areacode: ')
    
    raw_list = collect_data(data, size, areacode)

    print(raw_list)
    val_list = raw_list[1]

    print('Current data, please enter the fixed data as a list')
    print(val_list)

    val_list = [int(x) for x in input().split(', ')]

    if input('Continue?') == 'q':
        return False
    else:
        write_data(data, size, filename, areacode, val_list)

