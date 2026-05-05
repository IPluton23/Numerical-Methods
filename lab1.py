import numpy as np

xl, xr = 0, 1
tolerance = 1e-8
xm = (xr + xl) / 2
i=0

while abs((xr-xl)/xm)>tolerance:
    if (np.cos(xl)-xl)*(np.cos(xm)-xm)>0:
        xl=xm
    else:
        xr=xm
    xm = (xr + xl) / 2
    i+=1
print(round(xl, 8))
print(i)