import math

# Definition of functions
def f1(x):
    return math.cos(x) - x

def f1_prime(x):
    return -1 * math.sin(x) - 1

def f2(x):
    return (6435 * x**8 - 12012 * x**6 + 6930 * x**4 - 1260 * x**2 + 35) / 128

def f2_prime(x):
    return (8 * 6435 * x**7 - 6 * 12012 * x**5 + 4 * 6930 * x**3 - 2 * 1260 * x) / 128

def f3(x):
    return x**3 - 169

def f3_prime(x):
    return 3 * x**2

# Choose function
print("Choose the function:")
print("(1) cos(x) - x ; (2) P(x) ; (3) x^3 - 169")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        f = f1
        f_prime = f1_prime
    case 2:
        f = f2
        f_prime = f2_prime
    case 3:
        f = f3
        f_prime = f3_prime
    case _:
        print("Invalid choice, cos(x) - x is taken by default")
        f = f1
        f_prime = f1_prime

# Enter parameters
xOld = float(input("Enter x0: "))
Tolerance = float(input("Enter Tolerance: "))

# Initial values
i = 0 # to count iterations
Error = Tolerance + 1 # to start the while loop

# Do Newton-Raphson
while Error > Tolerance:
    xNew = xOld - (f(xOld) / f_prime(xOld))
    Error = abs((xNew - xOld) / xNew)
    i = i + 1
    print(f"i= {i} x0= {xNew:.8f}")
    xOld = xNew

# Prints the results
print(f"Root found at {xNew:.8f}")
print("Number of iterations:", i)