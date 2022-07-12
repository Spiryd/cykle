import random
from statistics import mean


def shuffle(n):
    """generuje randomową permutracje przez Fisher-Yates shuffle dla Sn"""
    base = list(range(1, n+1))
    permutation = []
    for i in range(len(base)):
        temp = random.randint(0, (len(base)-1))
        permutation.insert(0, base[temp])
        base.pop(temp)
    return permutation

def cycler(permutation):
    """rozkłada permutacje na cykle"""
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
    """testuje kod i dodaje wyniki do pliku csv"""
    f = open("test.csv", 'w')
    f.write("n;avrage number of cycles cycles\n")
    for n in range(1, 101):
        lengths = []
        for i in range(8000):
            lengths.append(len(cycler(shuffle(n))))
        row = str(n) + ";" + str(mean(lengths)) + "\n"
        f.write(row)
    f.close()
    
def zadanie():
    """numeryczny eksperyment, zadanie główne"""
    f = open("zadanie.csv", 'w')
    f.write("n;avrage max length of a cycle in a permutation\n")
    for n in range(1, 101):
        maxLengths = []
        for i in range(8000):
            maxLengths.append(max(len(c) for c in cycler(shuffle(n))))
        row = str(n) + ";" + str(mean(maxLengths)) + "\n"
        f.write(row)    
    f.close()
        
def main():
    """interfejs do programu"""
    menu_options = {
    1: 'Test',
    2: 'Zadanie',
    0: 'Exit',
    }
    while(True):
        for key in menu_options.keys():
            print(key, '-', menu_options[key])
        choice = int(input('Enter your choice: '))
        match choice:
            case 1:
                test()
            case 2:
                zadanie()
            case 0:
                exit()
            case _:
                print("Wrong input")

if __name__ == "__main__":
    main()
