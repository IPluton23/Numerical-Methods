import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x * math.exp(x)
def fprime(x):
    return math.exp(x) + math.exp(x) * x


def fda_fprime(x, h):
    return (f(x+h) - f(x)) / h
def fda_fbis(x, h):
    return (f(x) - 2*f(x+h) + f(x+2*h)) / (h**2)

def cda_fprime(x, h):
    return (f(x+h) - f(x-h)) / (2*h)
def cda_fbis(x, h):
    return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)


def calculate_slope(n, tab_x, tab_y):
    sum_x = 0
    sum_y = 0
    sum_xsq = 0
    sum_xy = 0

    for i in range(len(tab_x)):
        sum_x += tab_x[i]
        sum_y += tab_y[i]
        sum_xsq += tab_x[i]**2
        sum_xy += tab_x[i]*tab_y[i]

    return (n*sum_xy - sum_x*sum_y) / (n*sum_xsq - sum_x**2)

h_list = [x/100 for x in range(5, 51, 5)]
n = len(h_list)
fprime1, fprime2, fbis1, fbis2 = [0]*n, [0]*n, [0]*n, [0]*n # so we can iterate it
error_fda, error_cda = [0]*n, [0]*n

for i in range(len(h_list)):
    fprime1[i] = fda_fprime(2, h_list[i])
    fbis1[i] = fda_fbis(2, h_list[i])
    fprime2[i] = cda_fprime(2, h_list[i])
    fbis2[i] = cda_fbis(2, h_list[i])

    error_fda[i] = abs(fprime1[i] - fprime(2))
    error_cda[i] = abs(fprime2[i] - fprime(2))

ln_h = [math.log(x) for x in h_list]
ln_e2 = [math.log(x) for x in error_fda]
ln_e1 = [math.log(x) for x in error_cda]

print(fprime1, '\n', fbis1, '\n', error_fda, '\n', fprime(2), '\n')
print(fprime2, '\n', fbis2, '\n', error_cda)

print('First slope: ', calculate_slope(n, ln_h, ln_e1))
print('Second slope: ', calculate_slope(n, ln_h, ln_e2))

plt.plot(ln_h, ln_e1, marker='o')
plt.plot(ln_h, ln_e2, marker='v')
plt.show()