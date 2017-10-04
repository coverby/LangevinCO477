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

def test_temp_distribution():
    nsam = 1000
    temp = np.full(nsam,300)
    damp = np.full(nsam,.123)
    mean = np.zeros(nsam)
    samples = lang.gdist(mean,temp,damp)
    print(len(samples))
    assert(np.absolute(np.average(samples)) <= 5)

#def test_integrator_conserve_potential():
    #Solvent interactions + potential = cpnserves expected potential energy

#def test_integrator_conserve_KE():
    #Considering only potential = conserved KE

#def test_integrator_conserve_temp():
    #Solvent + random + potential energy = constant T