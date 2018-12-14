import parser
import math
import numpy as np
import matplotlib.pyplot as plt

def find_years(data):
    a1 = int(min(data[0]))
    a2 = int(max(data[0]))
    print('setting limits a1 =', a1, 'a2 =',a2)

    return np.r_[a1:a2:5], a1, a2

def find_yamp(data):
    try:
        y1 = int(math.trunc(min(data[1])/100)*100)
        y2 = int(math.trunc(max(data[1])/100)*100)
        delta = y2 - y1
        print('setting amps y1 =', y1, 'y2 =', y2)

    except TypeError as e:
        print('\033[31m' + 'Error: ' + '\033[0m'+ str(e))
        y1 = int(math.trunc(min(i for i in data[1] if i is not None)/100)*100)
        y2 = int(math.trunc(max(j for j in data[1] if j is not None)/100)*100)
        delta = y2 - y1

    if delta <= 1000:
        n = 100

    elif 2500 >= delta > 1000:
        n = 200

    elif 5000 >= delta > 2500:
        n = 500

    elif 7500 >= delta > 5000:
        n = 1000

    elif 10000 >= delta > 7500:
        n = 1500

    elif delta > 10000:
        n = 2000

    return np.r_[y1:y2+100:n]

def plotter(data, size):
    while True:
        xamp, a1, a2 = find_years(data)
        yamp = find_yamp(data)
        print(xamp, yamp)
        plt.plot(data[0], data[1], linewidth=3)
        plt.yticks(yamp)
        plt.xticks(xamp)
        plt.grid(True)
        plt.xlabel('Vuosi')
        plt.ylabel('Väestö')
        plt.suptitle('Väestö {:d}–{:d}'.format(a1, a2), fontweight='bold')
        plt.show()
        
        exit = input('Exit plotting mode? (y/n)')

        if exit == 'y':
            break
