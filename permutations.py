import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
from statistics import mean


def shuffle(given):
    """generates a random permutation with a Fisher-Yates shuffle"""
    permutation = []
    for i in range(len(given)):
        temp = random.randint(0, (len(given)-1))
        permutation.insert(0, given[temp])
        given.pop(temp)
    return permutation

def cycle(permutation):
    """turns a permutation into cycles """
    cycles = []
    for i in range(1, len(permutation) + 1):
        if permutation[i - 1] != 0: 
            temp = i
            cycle = []
            cycle.append(i)
            while permutation[temp - 1] != i:
                cycle.append(permutation[temp - 1])
                temp = permutation[temp - 1]
            cycles.append(cycle)
            for j in cycle: 
                permutation[permutation.index(j)] = 0
    return cycles

def test():
    """tests the code and writes it to a csv file"""
    f = open("test.csv", 'w')
    f.write("n;avrage number of cycles cycles\n")
    for i in range(1, 101):
        lengths = []
        for j in range(8000):
            x = list(range(1, i + 1))
            lengths.append(len(cycle(shuffle(x))))
        row = str(i) + ";" + str(mean(lengths)) + "\n"
        f.write(row)
    f.close()
        
def main():
    menu_options = {
    1: 'Test',
    0: 'Exit',
    }
    while(True):
        for key in menu_options.keys():
            print(key, '-', menu_options[key])
        choice = int(input('Enter your choice: '))
        match choice:
            case 1:
                test()
            case 0:
                exit()
            case _:
                print("Wrong input")

if __name__ == "__main__":
    main()