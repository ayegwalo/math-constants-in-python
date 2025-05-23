import math

# first pi 
pi = math.pi
print("First Pi from module:", pi)

# second pi
second_pi = 4 * math.atan(1)
print("Second Pi from arc tan identity:", second_pi)

# third pi
def compute_pi(n_terms=100000):
    return 4 * sum ((-1)**k / (2*k + 1) for k in range(n_terms))
third_pi = compute_pi()
print("Third Pi form infinite series(Leibniz formula):", third_pi)


# Euler's Number
e1 = math.e
print("Euler number from module:", e1)

# Limit definition
def compute_e2(n=100000):
    return (1 + 1/n)**n
second_e = compute_e2()
print("Euler number from Limit definition:", second_e)

# Series expansion
def compute_e3(n_terms=20):
    return sum(1/math.factorial(k) for k in range(n_terms))
third_e = compute_e3()
print("Euler number from Series expansion:", third_e)


# Euler-Mascheroni Constant

# 1. Numerical approximation
def compute_gamma1(n=1000000):
    return sum(1/k for k in range(1, n+1)) - math.log(n)
gamma1 = compute_gamma1()
print("Euler-Mascheroni Constant from Numerical approximation:", gamma1)
