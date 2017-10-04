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

#def start():
#    print("LangevinCo477 start succeeded.")


                
async def main(sv):
    #create a simple energy

    x = np.linspace(-1, 1, 100)
    y = x**2
    sv.set_energy(x, y)



    while True:
        sv.set_position(np.random.random(1))
        await asyncio.sleep(0.5)



def start():
    sv = SimVis()
    start_server(sv)
    asyncio.ensure_future(main(sv))
    loop = asyncio.get_event_loop()
    loop.run_forever()