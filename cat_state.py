import numpy as np
from math import factorial, sqrt

def coherent_state(alpha, N):
    coeffs = np.zeros(N, dtype=complex)
    prefactor = np.exp(-abs(alpha)**2 / 2)
    for n in range(N):
        coeffs[n] = prefactor * alpha**n / sqrt(factorial(n))
    return coeffs

def cat_state(alpha, N, parity="even"):
    # positive and negative parts of cat state
    negative = coherent_state(alpha, N)
    positive = coherent_state(-alpha, N)

    if parity == "even":
        psi = positive + negative
    elif parity == "odd":
        psi = positive - negative
    else:
        raise ValueError("parity must be 'even' or 'odd'")

    psi /= np.linalg.norm(psi)
    return psi