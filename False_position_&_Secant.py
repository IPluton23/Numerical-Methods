import math

def f(x):
    return math.cos(x)-x


def falsePositionMethod(xLeft, xRight):
    tolerance = 1e-8
    error = tolerance+1 # Just to start while loop
    count = 0
    xBefore = xLeft
    while error > tolerance:
        count += 1
        x0 = (xLeft*f(xRight) - xRight*f(xLeft)) / (f(xRight) - f(xLeft))
        if f(x0)*f(xLeft) < 0:
            xBefore = xRight
            xRight = x0
        else:
            xBefore = xLeft
            xLeft = x0
        error = abs((x0 - xBefore)/x0)
    return x0, count

def secantMethod(xBefore, xCurrent):
    tolerance = 1e-8
    error = tolerance+1
    count = 0
    while error > tolerance:
        count += 1
        xNext = (xBefore*f(xCurrent) - xCurrent*f(xBefore)) / (f(xCurrent) - f(xBefore))
        error = abs((xNext - xCurrent)/xNext)
        xBefore = xCurrent
        xCurrent = xNext
    return xCurrent, count

        
result = falsePositionMethod(0, 1)
print("Root found at: ", round(result[0], 8), " with False-Position Method.\nNumber of iterations: ", result[1])
result = secantMethod(0, 1)
print("\n\nRoot found at: ", round(result[0], 8), " with Secant Method.\nNumber of iterations: ", result[1])
