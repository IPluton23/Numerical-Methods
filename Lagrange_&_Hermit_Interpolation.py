import math
import matplotlib.pyplot as plt

def f1(x):
    return math.exp(x)
def f1Prime(x):
    return math.exp(x)

def f2(x):
    return 1/(1+x**2)
def f2Prime(x):
    return -2*x/(1+x**2)**2


def lagrange_interpolation(x, x_points, f):
    result = 0

    for j in range(len(x_points)):
        lj = 1
        for i in range(len(x_points)):
            if i != j:
                lj *= (x - x_points[i])/(x_points[j] - x_points[i])

        result += lj*f(x_points[j])
    return result


def hermite_interpolation(x, x_points, f, fPrime):
    result = 0
    for j in range(len(x_points)):

        lj = 1
        for i in range(len(x_points)):
            if i != j:
                lj *= (x-x_points[i]) / (x_points[j] - x_points[i])

        ljPrime = 0
        for i in range(len(x_points)):
            if i != j:
                ljPrime += 1 / (x_points[j] - x_points[i])

        hj = (1 - 2*(x - x_points[j]) * ljPrime) * lj**2
        hjMean = (x - x_points[j]) * lj**2

        result += (hj * f(x_points[j])) + (hjMean * fPrime(x_points[j]))
    return result


interval = [x/10 for x in range(-50, 51)] # interval on which we will calculate polynomynals p(x)

print("Wybierz funkcje interpolowaną:\n (1) - e^x\t (2) 1/(1+x^2)")
choice = int(input())
if choice == 1:
    f = f1
    fPrime = f1Prime
    x_points = [-1, 0.5, 1.5, 2]
else:
    f = f2
    fPrime = f2Prime
    x_points = list(range(-5, 6))


print("Wybierz metode interpolacji:\n (1) - Lagrange\t (2) - Hermite")
choice = int(input())
if choice == 1:
    y_result = [lagrange_interpolation(x, x_points, f) for x in interval]
else:
    y_result = [hermite_interpolation(x, x_points, f, fPrime) for x in interval]

print(y_result)

plt.plot(interval, y_result, marker='o')
plt.grid(True)
plt.show()

