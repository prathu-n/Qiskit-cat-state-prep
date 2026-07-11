# Qiskit-cat-state-prep

# Variational Preparation and Simulation of Bosonic Cat States on a Qubit-Based Quantum Computer

## Overview

Bosonic qubits are an approach to quantum computing in which quantum information is encoded in harmonic oscillators rather than two level qubits. Some examples are binomial encodings and cat qubits, which are hardware efficient solutions to quantum error correction.

While bosonic qubits are naturally implemented in superconducting microwave cavities, gate based quantum computers operate using finite collections of qubits. This project explores how bosonic quantum states can be approximately represented and prepared on a qubit based architecture using variational quantum circuits.

The primary objective is to implement a variational state preparation algorithm in Qiskit that prepares an approximation of a cat state after truncating the bosonic Hilbert space to a finite number of Fock states.



## Background

A bosonic mode has an infinite-dimensional Hilbert space


{|0\rangle, |1\rangle, |2\rangle, \ldots},


making it fundamentally different from a two-level qubit.

A cat state is a coherent superposition of two coherent states,


|\alpha^\pm\rangle = N_\pm \left( \alpha\rangle \pm |-\alpha\rangle \right),

where (\alpha) is the coherent state amplitude and (N_\pm) is a normalization factor.

Cat states naturally suppress certain error channels, particularly photon loss.

Since gate based quantum processors cannot natively realize infinite dimensional oscillators, we truncate the Hilbert space to the first (N) Fock states and encode those states into qubits.



## Goals

The project consists of four primary tasks:

- Construct truncated bosonic cat states in the Fock basis.
- Encode the truncated Hilbert space into qubits.
- Use a classical optimizer to construct a parameterized quantum circuit to prepare the target state.
- Evaluate the fidelity of the prepared state.



## Methodology

### 1. Truncated Bosonic Encoding

The infinite-dimensional oscillator is truncated to the first N Fock states.

These basis states are then mapped onto

\lceil \log_2 N \rceil

qubits.

For example,

|0\rangle) \rightarrow  000 \\
|1\rangle) \rightarrow  001 \\
|2\rangle) \rightarrow  010 \\



### 2. Target State

The target state is an even or odd cat state projected into the truncated Hilbert space.


### 3. Variational State Preparation

A parameterized quantum circuit is constructed using Qiskit.

Circuit parameters are optimized using a classical optimizer to maximize

F = |\langle\psi_{\mathrm{target}} |\psi(\theta)\rangle|^2,

where (\psi_{\mathrm{target}}) is the truncated cat state, and (\psi(\theta)) is the variational state.


## References

1. S. Puri et al., *Bias-Preserving Gates with Stabilized Cat Qubits*, Science Advances **6**, eaay5901 (2020).

2. A. Grimm et al., *Stabilization and Operation of a Kerr-Cat Qubit*, Nature **584**, 205–209 (2020).

3. C. Chamberland et al., *Building a Fault-Tolerant Quantum Computer Using Concatenated Cat Codes*, PRX Quantum **3**, 010329 (2022).

4. M. Mirrahimi et al., *Dynamically Protected Cat-Qubits: A New Paradigm for Universal Quantum Computation*, New Journal of Physics **16**, 045014 (2014).

5. S. Ofek et al., *Extending the Lifetime of a Quantum Bit with Error Correction in Superconducting Circuits*, Nature **536**, 441–445 (2016).
