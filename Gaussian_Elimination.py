def gauss_elimination(a, b, c, r):
    x = [0] * 5 # just to iterate it
    beta = [0] * 5
    rho = [0] * 5
    beta[0] = b[0]
    rho[0] = r[0]

    for j in range(1, len(r)):
        beta[j] = b[j] - a[j-1] * c[j-1] / beta[j-1]    # we use a[j-1] instead of a[j] (as in instruction) to prevent out-of-range error
        rho[j] = r[j] - a[j-1] * rho[j-1] / beta[j-1]   # its because there are 4 values of a, but indexing (in instruction) start from 2

    n = len(r)-1
    x[n] = rho[n]/beta[n]

    for j in range(len(r)-2, -1, -1):
        x[j] = (rho[j] - c[j] * x[j+1])/(beta[j])

    return x


diagonal_c = [-1] * 4
diagonal_b = [2] * 5
diagonal_a = [-1] * 4
r = [0, 1, 2, 3, 4]

gauss = gauss_elimination(diagonal_a, diagonal_b, diagonal_c, r)
if __name__ == '__main__':
    for i in gauss:
        print(round(i, 5))
