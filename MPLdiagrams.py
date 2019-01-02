import parser
import math
from numpy import r_
import matplotlib.pyplot as plt

def find_years(data):
    a1 = int(min(data[0]))
    a2 = int(max(data[0]))
    print('setting limits a1 =', a1, 'a2 =',a2)

    return r_[a1:a2:5], a1, a2

def find_yamp(data):
    try:
        if max(data[1]) < 10000:
            div = 100
        else:
            div = 1000

        y1 = int(math.trunc(min(data[1])/div)*div)
        y2 = int(math.trunc(max(data[1])/div)*div)
        delta = y2 - y1
        print('setting amps y1 =', y1, 'y2 =', y2)

    except TypeError as e:
        if max(i for i in data[1] if i is not None) < 10000:
            div = 100
        else:
            div = 1000

        print('\033[31m' + 'Error: ' + '\033[0m'+ str(e))
        y1 = int(math.trunc(min(i for i in data[1] if i is not None)/div)*div)
        y2 = int(math.trunc(max(j for j in data[1] if j is not None)/div)*div)
        delta = y2 - y1

    if delta <= 1000:
        n = 100
        o = 50

    elif 2500 >= delta > 1000:
        n = 200
        o = 100

    elif 5000 >= delta > 2500:
        n = 500
        o = 250

    elif 7500 >= delta > 5000:
        n = 1000
        o = 500

    elif 10000 >= delta > 7500:
        n = 1500
        o = 750

    elif 15000 >= delta > 10000:
        n = 2000
        o = 1000
    
    elif 20000 >= delta > 15000:
        n = 3000
        o = 1500

    elif delta > 20000:
        n = 5000
        o = 2500

    return r_[y1:y2+o:n]

def plotter(areacode, data, size, mode, filedir):
    while True:
        xamp, a1, a2 = find_years(data)
        yamp = find_yamp(data)
        print(xamp, yamp)
        plt.figure(figsize=(8,4.84))
        plt.plot(data[0], data[1], linewidth=3)
        plt.yticks(yamp)
        plt.xticks(xamp)
        plt.grid(True)
        plt.xlabel('Vuosi')
        plt.ylabel('Väestö')
        plt.suptitle('Väestö {:d}–{:d}'.format(a1, a2), fontweight='bold')

        if mode == 'visual':
            plt.show()
            
            exit = input('Exit plotting mode? (q/n)')
            if exit == 'q':
                break

        elif mode == 'svg':
            filename = str(filedir + areacode + '.svg')
            plt.savefig(filename, format='svg')
            plt.close()
            break

