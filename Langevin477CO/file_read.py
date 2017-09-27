import numpy as np

def read_energy(input_file):
    pos = []
    energy = []
    data = np.genfromtxt(input_file, delimiter = "   ")
    L1 = []
    for row in data:   
        pos.append(data[0])
        energy.append(data[1]) 
    return pos, energy