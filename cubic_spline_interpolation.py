import math
import matplotlib.pyplot as plt
from Gaussian_Elimination import gauss_elimination


def f(x):
    return 1/(1+x**2)


def calculate_bot_diagonal(step, size):
    bottom_diagonal = [step] * (size - 3)
    bottom_diagonal.insert(0, 0)
    bottom_diagonal.append(0)
    return bottom_diagonal


def calculate_main_diagonal(step, size):
    main_diagonal = [4 * step] * (size - 2)
    main_diagonal.insert(0, 1)
    main_diagonal.append(1)
    return main_diagonal


def calculate_top_diagonal(step, size):
    top_diagonal = [step] * (size - 3)
    top_diagonal.insert(0, 0)
    top_diagonal.append(0)
    return top_diagonal

def calculate_r(step, size):
    r = [0]
    for j in range(1, size - 1):
        r.append(6 * (pj[j + 1] - 2 * pj[j] + pj[j - 1]) / step)
    r.append(0)
    return r


def cubic_spline_interpolation(xj ,pj, pbis, step, size, points):
    p = [0]*len(points)
    for j in range(size):
        for i in range(len(points)):
            x = points[i]
            if xj[j] <= x < xj[j+1]:
                p[i] = pj[j] + ( (pj[j+1] - pj[j])/step - step*pbis[j+1]/6 - step*pbis[j]/3)*(x - xj[j]) + (pbis[j]/2)*(x - xj[j])**2 + ((pbis[j+1] - pbis[j])/6*step)*(x - xj[j])**3
            else:
                continue
    return p


xj = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]     # known x
pj = [f(x) for x in xj]                         # known f(x)
h = 1                                           # step
n = 11                                          # number of known points (size of interval)
x = [x/10 for x in range(-50, 50, 1)]           # points to interpolate
top_diagonal = calculate_top_diagonal(h, n)
main_diagonal = calculate_main_diagonal(h, n)
bottom_diagonal = calculate_bot_diagonal(h, n)
r = calculate_r(h, n)

p_bis = gauss_elimination(bottom_diagonal, main_diagonal, top_diagonal, r)

result = cubic_spline_interpolation(xj, pj, p_bis, h, n, x)
print(result)
plt.plot(x, result, marker='o')
plt.show()