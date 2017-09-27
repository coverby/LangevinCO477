import io
import numpy as np
import Langevin477CO as lang


def test_read_energy_read():
    '''Tests if the function reads and returns given an input file'''
    test_string = '''
    #test input energy
    #x energy 
    0   -2
    1   -1
    2   0
    3   0
    4   3
    '''

    test_file = io.StringIO(test_string)
    pos, energy = lang.read_energy(test_file)
    #print(pos)
    #print(energy)
    #print((np.isclose(pos, [0,1,2,3,4])).any())
    assert((np.isclose(pos, [0,1,2,3,4])).any())
    assert((np.isclose(energy,[-2,-1,0,0,3])).any())