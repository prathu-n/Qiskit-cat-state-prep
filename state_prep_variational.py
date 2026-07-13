import numpy as np
from scipy.optimize import minimize
from qiskit.circuit.library import real_amplitudes
from qiskit.quantum_info import Statevector

def num_qubits(N):
    # number of qubits needed to represent N Fock levels
    return int(np.ceil(np.log2(N)))

def embed_state(state, num_qubits):
    dim = 2**num_qubits
    if len(state) > dim:
        raise ValueError("State is larger than qubit Hilbert space.")
    embedded = np.zeros(dim, dtype=complex)
    embedded[:len(state)] = state
    return embedded

def make_ansatz(num_qubits, reps):
    ansatz = real_amplitudes(
    num_qubits=num_qubits,
    reps=reps,
    entanglement="linear"
)
    return ansatz

def fidelity(target, trial):
    overlap = np.vdot(target, trial)
    return np.abs(overlap)**2

def cost_function(theta, ansatz, target_state):
    circuit = ansatz.assign_parameters(theta)
    trial_state = Statevector.from_instruction(circuit)
    F = fidelity(target_state, trial_state.data)
    return 1 - F


# initial_theta = np.random.uniform(
#     0,
#     2*np.pi,
#     ansatz.num_parameters
# )

def optimize_circuit(ansatz, initial_theta, target_state, maxiter=100):
    history = []
    def history_update(theta):
        cost = cost_function(theta, ansatz, target_state)
        history.append(1 - cost)
        # print(f"Iteration {len(history)}: Fidelity = {1 - cost}")

    result = minimize(
        cost_function,
        initial_theta,
        args=(ansatz, target_state),
        method="COBYLA",
        callback=history_update,
        options={"maxiter": maxiter}
    )

    # print(result.success)
    # print(result.message)
    # print("Final fidelity:", 1 - result.fun)

    best_theta = result.x
    optimized_circuit = ansatz.assign_parameters(best_theta)
    optimized_state = Statevector.from_instruction(optimized_circuit)
    
    return optimized_circuit, optimized_state, history