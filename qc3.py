from qiskit import QuantumCircuit,  QuantumRegister
from qiskit.quantum_info import Statevector
from math import pi
import qiskit
import numpy as np
import qiskit.quantum_info as qi

def figure_it_out_1():
    """ Simplify the circuit from the test with the strategies we saw in class. You should get
        get a circuit with at most 3 gates. This will be inspected manually. If you pass the test with
        more gates, you will get a 0 as your grade (A swap gate or a cnot gate counts as 1 gate)

    Args: 
        None
    """
    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    #begins your code
    qc.x(0)
    qc.swap(1,0)
    qc.x(1)
    #ends your code
    return qi.Operator(qc)

def figure_it_out_2():
    """ Simplify the circuit from the test with the strategies we saw in class. You should get
        get a circuit with at most 4 gates. This will be inspected manually. If you pass the test with
        more gates, you will get a 0 as your grade (A swap gate or a cnot gate counts as 1 gate)

    Args: 
        None
    """
    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    #begins your code 
    qc.h(0)
    qc.swap(1,0)
    #ends your code 
    return qi.Operator(qc)

def figure_it_out_3():
    """ Simplify the circuit from the test with the strategies we saw in class. You should get
        get a circuit with at most 3 gates. This will be inspected manually. If you pass the test with
        more gates, you will get a 0 as your grade (A swap gate or a cnot gate counts as 1 gate)

    Args: 
        None
    """
    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    #begins your code 
    qc.h(1)
    qc.h(0)
    qc.z(0)
    #ends your code 
    return qi.Operator(qc)

