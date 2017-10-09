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
    273 .123    0.001   10
    '''
    test_file = io.StringIO(test_string)
    temp, damp, tstep, totaltime = lang.read_coefficients(test_file)

    assert(np.isclose(temp,273))
    assert(np.isclose(damp, .123))
    assert(np.isclose(tstep,0.001))
    assert(np.isclose(totaltime, 10))

def test_temp_distribution():
    nsam = 1000
    temp = 300
    damp = .123
    mean = np.zeros(nsam)
    samples = lang.gdist(mean, temp, damp)
    print(len(samples))
    if np.absolute(np.average(samples)) >= 5:
        newavg = 0
        for i in range(3):
            samples1 = lang.gdist(mean, temp, damp)
            newavg += np.average(samples1)
            samples1 = []
        assert(newavg <= 15)

def test_core_integrator_setup():
    xi = 1
    vi = 1
    ui = 1
    fi = 1
    la = .123
    temp = 300
    mass = 1
    tstep = .01
    totaltime = 10
    output = lang.core_integrator(xi,vi,ui,fi,la,temp,mass,tstep,totaltime)
    print("Number of output variables: ")
    print(len(output))
    assert(len(output) == 5)
    print("Length of each output: ")
    print(len(output[0]))
    assert(len(output[0]) == int(np.floor(totaltime/tstep) ))

def test_integrator_conserve_potential():
    #Solvent interactions + potential = conserves expected potential energy
    xi = 1
    vi = 1
    ui = 1
    fi = 1
    la = 0.123
    temp = 0
    mass = 1
    tstep = .001
    totaltime = 100
    output = lang.core_integrator(xi,vi,ui,fi,la,temp,mass,tstep,totaltime)
    print("Potential energy format looks like:")
    print(output[3])
    print("Average potential energy over time looks like:")
    print(np.average(output[3]))
    assert(np.isclose(np.average(output[3]),0))

def test_integrator_conserve_KE():
    #Considering only potential = conserved KE
    xi = 1
    vi = 1
    ui = 1
    fi = 1
    la = 0
    temp = 300
    mass = 1
    tstep = .001
    totaltime = 100
    output = lang.core_integrator(xi,vi,ui,fi,la,temp,mass,tstep,totaltime)
    print("Potential energy format looks like:")
    print(output[3])
    print("Average potential energy over time looks like:")
    print(np.average(output[3]))
    print("Position format looks like:")
    print(output[0])
    print("Average position over time looks like:")
    print(np.average(output[0]))
    assert(np.isclose(np.average(output[3]),ui))

#def test_integrator_conserve_temp():
   #Solvent + random + potential energy = constant T