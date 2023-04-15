from fractions import Fraction
import math
import matplotlib.pyplot as plt
import numpy as np

# Function definitions

def p_adic_valuation(n, p):
    """Returns the p-adic valuation of a number n."""
    if n == 0:
        return float('inf')
    valuation = 0
    while n % p == 0:
        n //= p
        valuation += 1
    return valuation

def p_adic_distance(a, b, p):
    """Returns the p-adic distance between two integers a and b."""
    return p ** (-p_adic_valuation(abs(a - b), p))

def lcm(a, b):
    """Return the least common multiple of two integers."""
    return abs(a * b) // math.gcd(a, b)

def p_adic_distance_rational(a, b, p):
    """Returns the p-adic distance between two rational numbers a and b."""
    a_frac = Fraction(a).limit_denominator()
    b_frac = Fraction(b).limit_denominator()
    
    lcm_denominators = lcm(a_frac.denominator, b_frac.denominator)
    
    a_int = a_frac.numerator * (lcm_denominators // a_frac.denominator)
    b_int = b_frac.numerator * (lcm_denominators // b_frac.denominator)
    
    return p_adic_distance(a_int, b_int, p)

# Parameters
range_max = 10
p = 2

# Integer plot
"""
x_int = list(range(0, range_max + 1))
y_int = list(range(0, range_max + 1))
z_int = np.zeros((len(y_int), len(x_int)))

for i, a in enumerate(y_int):
    for j, b in enumerate(x_int):
        z_int[i, j] = p_adic_distance(a, b, p)

plt.imshow(z_int, origin='lower', cmap='viridis', extent=[0, range_max, 0, range_max], aspect='auto')
plt.colorbar(label=f'{p}-adic distance')
plt.xlabel('a')
plt.ylabel('b')
plt.title(f'{p}-adic Distance over Integers')
plt.grid()
plt.show()
"""
# Rational plot
fidelity = 128
step = 1 / fidelity  # Step size for rational numbers
x_rat = [x * step for x in range(fidelity * range_max + 1)]
y_rat = [y * step for y in range(fidelity * range_max + 1)]
z_rat = np.zeros((len(y_rat), len(x_rat)))

for i, a in enumerate(y_rat):
    for j, b in enumerate(x_rat):
        z_rat[i, j] = p_adic_distance_rational(a, b, p)

plt.imshow(z_rat, origin='lower', cmap='jet', extent=[0, range_max, 0, range_max], aspect='auto')
plt.colorbar(label=f'{p}-adic distance')
plt.xlabel('a')
plt.ylabel('b')
plt.title(f'{p}-adic Distance over Rational Numbers')
plt.grid()
plt.show()
