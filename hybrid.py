import math

# function definitions
def f1(x):
    return (6435*x**8 - 12012*x**6 + 6930*x**4 - 1260*x**2 + 35)/128
def f1Prime(x):
    return (8*6435*x**7 - 6*12012*x**5 + 4*6930*x**3 - 2*1260*x)/128

def f2(x):
    return x**2 - 2*x - 2
def f2Prime(x):
    return 2*x - 2


#initial values
tolerance = 1e-8
Error = tolerance+1 #to start while
print("Choose a function:")
print("(1) Polynomial; (2) x^2 - 2x - 2")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        f = f1
        fPrime = f1Prime
        xLeft = 0.4
        xRight = 0.7
    case 2:
        f = f2
        fPrime = f2Prime
        xLeft = 0
        xRight = 3
    case _:
        print("Invalid choice, function 1 is taken as default")
        f = f1
        fPrime = f1Prime
        xLeft = 0.4
        xRight = 0.7


while Error>tolerance:
    # check if to use N-R or Bisection
    if (fPrime(xLeft))>0:
        if (xLeft-xRight)*fPrime(xLeft) - f(xLeft) <= 0:    #N-R method
            xNew = xLeft - f(xLeft)/fPrime(xLeft)
        else:                                               # bisection
            xNew = (xLeft+xRight)/2
        # new interval
        if xNew > xLeft:
            xRight = xNew
        else:
            xLeft = xNew
    else:
        if (xLeft-xRight)*fPrime(xLeft) - f(xLeft) >= 0:    # N-R
            xNew = xLeft - f(xLeft)/fPrime(xLeft)
        else:
            xNew = (xLeft+xRight)/2                         # bisection
        # new interval
        if xNew > xLeft:
            xRight = xNew
        else:
            xLeft = xNew
    Error = abs((xNew-xLeft)/xNew)   
