import io
import numpy as np
import Langevin477CO as lang


def test_read_energy_read():
    '''Tests if the function reads and returns given an input file'''
    test_string = '''
    #test input energy
    #i  x   energy  fx 
    0   0   0   -2
    1   0   1   -1
    2   0   2   4
    3   0   4   6
    4   3   0   1
    '''

    test_file = io.StringIO(test_string)
    indx, pos, energy, fx = lang.read_energy(test_file)
    #print(pos)
    #print(energy)
    #print((np.isclose(pos, [0,1,2,3,4])).any())
    assert((np.isclose(indx, [0,1,2,3,4])).any())
    assert((np.isclose(pos, [0,0,0,0,3])).any())
    assert((np.isclose(energy,[0,1,2,4,0])).any())
    assert((np.isclose(fx, [-2,-1,4,6,1])).any())


def test_read_coefficients_read():
    test_string = '''
    #Test coefficient string
    #temp   damping     
    273 .123
    '''
    test_file = io.StringIO(test_string)
    temp, damp = lang.read_coefficients(test_file)

    assert(np.isclose(temp,273))
    assert(np.isclose(damp, .123))