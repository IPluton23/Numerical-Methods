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
tolerance = 10e-8
Error = tolerance+1 #to start while
countNR, countBS = 0, 0


print("Choose a function: (default option is 2)")
print("(1) Polynomial; (2) x^2 - 2x - 2")
choice = int(input("Enter your choice: "))
if choice == 1:
    f = f1
    fPrime = f1Prime
    xLeft = 0.4
    xRight = 0.7
else:
    f = f2
    fPrime = f2Prime
    xLeft = 0
    xRight = 3

xCurrent = xLeft
xNew = xLeft
while Error>tolerance:
    LT = (xNew - xLeft) * fPrime(xNew) - f(xNew)
    RT = (xNew - xRight) * fPrime(xNew) - f(xNew)

    # check if to use N-R or Bisection
    if LT*RT <= 0:                                      #N-R method
        xNew = xCurrent - f(xCurrent)/fPrime(xCurrent)
        countNR += 1
    else:                                               # bisection
        xNew = (xLeft+xRight)/2
        countBS += 1

    # new interval
    if f(xNew)*f(xLeft)<0:
        Error = abs((xNew - xRight) / xNew)
        xRight = xNew
    else:
        Error = abs((xNew - xLeft) / xNew)
        xLeft = xNew
    xCurrent = xNew


print("Root found at: ", round(xLeft, 8))
print("Iterations for N-R: ", countNR)
print("Iterations for bisection: ", countBS)
