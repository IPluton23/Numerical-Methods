import math

def f(x):
    return math.sin(x)
def exactInt(x):
    return -math.cos(x)

def fPrime(x):
    return math.cos(x)
def fTrice(x):
    return -math.cos(x)

def calculateWidth(x0, xN, N):
    return (xN-x0)/N


def trapezoid(x0,h,N):
    result = 0
    for i in range(1, N+1):
        x_prev = x0 + (i-1)*h
        x_i = x0 + i*h
        result += 0.5*h*(f(x_prev) + f(x_i))
    return result


def simpson(x0,xN, h, N):
    result = f(x0) + f(xN)
    for i in range(1, int(N/2)+1):
        result += 4*f(x0 + (2*i-1)*h)
    for i in range(1, int(N/2)):
        result += 2*f(x0 + 2*i*h)
    return result*h/3


def boole(x0, xN, h, N):
    result = 7*(f(x0) + f(xN))
    for i in range(1, N):
        if i % 2 != 0:
            result += 32*f(x0 + i*h)
        else:
            if i/2 % 2 != 0:
                result += 12*f(x0 + i*h)
            else:
                result += 14*f(x0 + i*h)
    return result*2*h/45


def eulerMaclaurin(x0,xN,h,N):
    result = trapezoid(x0, h, N)
    result += (h**2)*(fPrime(x0) - fPrime(xN))/12 - (h**4)*(fTrice(x0) - fTrice(xN))/720
    return result


print('Choose method\t 1 - Trapezoid, 2 - Simpson, 3 -Boole, 4 - Euler-Maclaurin')
option = int(input())
if option == 1:
    data = [
        trapezoid(0, calculateWidth(0, math.pi, N), N)
        for N in [2 ** k for k in range(2, 11)]
    ]
    print(data)
elif option == 2:
    data = [
        simpson(0, math.pi, calculateWidth(0, math.pi, N), N)
        for N in [2 ** k for k in range(2, 11)]
    ]
    print(data)
elif option == 3:
    data = [
        boole(0, math.pi, calculateWidth(0, math.pi, N), N)
        for N in [2 ** k for k in range(2, 11)]
    ]
    print(data)
elif option == 4:
    data = [
        eulerMaclaurin(0, math.pi, calculateWidth(0, math.pi, N), N)
        for N in [2 ** k for k in range(2, 11)]
    ]
    print(data)
else:
    print('Wrong value. Program closed')
