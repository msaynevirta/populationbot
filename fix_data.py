import json
import os

def merge(data, data_dir, report_dir, size):
    val_list = []
  
    areacode1 = input('Please enter the first areacode: ')
    areacode2 = input('Please enter the second areacode: ')
    
    lab1 = data["dataset"]["dimension"]["Alue"]["category"]["label"][areacode1]
    lab2 = data["dataset"]["dimension"]["Alue"]["category"]["label"][areacode2]
    print('Merging {:s} to {:s}'.format(lab1, lab2))
    
    report_file = str(report_dir + 'merges.txt')
    with open(report_file, 'a') as f:
        f.write('Merged {:s} ({:s}) to {:s} ({:s})\n'.format(lab1, areacode1, lab2, areacode2))

def fix(data, filename, size): 
    val_list = [] 
    
    areacode = input('Please enter areacode: ')
    
    index = data["dataset"]["dimension"]["Alue"]["category"]["index"][areacode]
    start = i = size[2]*index #find the starting position of the population data 
 
    lab = data["dataset"]["dimension"]["Alue"]["category"]["label"][areacode]

    while i < start + size[2]:
        val = data["dataset"]["value"][i]
        val_list.append(val)
        i += 1

    print('Current data, please enter the fixed data as a list')
    print(val_list)
    val_list = [int(x) for x in input().split(', ')]
    i = start
    j = 0

    while i < start + size[2]:
        data["dataset"]["value"][i] = val_list[j]
        print(val_list[j])
        i += 1
        j += 1

    print('Values written')

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 5)
