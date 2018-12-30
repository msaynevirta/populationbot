# coding=utf-8

# PX-web json-tiedoston käsittely ja parsinta http://api.aluesarjat.fi/

# Lataaminen Wikimedia Commonsiin Pywikibotilla

def importJSON(filedir):
    import json
    data = json.load(open(filedir,"r", encoding='utf-8'))
    
    size = data["dataset"]["dimension"]["size"]
    
    return data, size
	
def areacodes_to_csv(data):
    d = data["dataset"]["dimension"]["Alue"]["category"]["label"]
    f = open("data/areacodes.csv", "w+")

    for key in d.items():
        f.write("{:10s},{:s}\n".format(key[0], key[1]))

    f.close()

def areacodes_to_list(data):
    list = []
    d = data["dataset"]["dimension"]["Alue"]["category"]["label"]

    for key in d.items():
        list.append(key[0])
    
    return list

def collect_data(data, size, areacode):
    main_list = []
    year_list = []
    val_list = []

    index = data["dataset"]["dimension"]["Alue"]["category"]["index"][areacode]
    year = 1975
    start = i = size[2]*index #find the starting position of the population data

    lab = data["dataset"]["dimension"]["Alue"]["category"]["label"][areacode]

    while i < start + size[2]:
        val = data["dataset"]["value"][i]
        year_list.append(year)
        val_list.append(val)
        i += 1
        year += 1

    main_list.append(year_list)
    main_list.append(val_list)
    return main_list

"""
def main():
	areacode = str(input("give areacode"))
	print(collect_data(areacode))
	
main()
"""

