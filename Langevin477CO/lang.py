import numpy as np
from .visualization import SimVis, start_server
import io
import asyncio

def read_energy(input_file):
    #datafile = io.StringIO(input_file)
    #print(input_file.getvalue())
    indx = []
    pos = []
    energy = []
    fx = []
    data = np.loadtxt(input_file)
    #print(data)
    #print(data[1][1])
    
    for row in range(len(data)):   
        indx.append(data[row][0])
        pos.append(data[row][1])
        energy.append(data[row][2])
        fx.append(data[row][3]) 
    return indx, pos, energy, fx

def read_coefficients(input_file):
    data = np.loadtxt(input_file)
    
    temp = data[0]
    damp = data[1]

    return temp, damp

def gdist(mean,temp,damp):
    #Generate Gaussian distribuuted nu
    sample = []
    var = np.multiply(np.multiply(2,temp),damp)
    for i in range(len(mean)):
        sample.append(np.random.normal(mean[i],var[i],1))
    return sample 

async def main(sv): #pragma: no cover
    #create a simple energy

    x = np.linspace(-1, 1, 100)
    y = x**2
    sv.set_energy(x, y)



    while True:
        sv.set_position(np.random.random(1))
        await asyncio.sleep(0.5)



def start(): #pragma: no cover
    sv = SimVis()
    start_server(sv)
    asyncio.ensure_future(main(sv))
    loop = asyncio.get_event_loop()
    loop.run_forever()