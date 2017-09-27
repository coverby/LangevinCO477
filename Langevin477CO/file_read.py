import numpy as np
import io

def read_energy(input_file):
    #datafile = io.StringIO(input_file)
    #print(input_file.getvalue())
    pos = []
    energy = []
    data = np.loadtxt(input_file)
    #print(data)
    #print(data[1][1])
    
    for row in range(len(data)):   
        pos.append(data[row][0])
        energy.append(data[row][1]) 
    return pos, energy