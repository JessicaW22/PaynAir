import math

def Taylor(x, n):
    e_approx = 0
    for i in range(n):
        e_approx += x**i/math.factorial(i)

    return e_approx

def err_e(x, threshold): 
    n = 1
    e_approx = Taylor(x, n)
    Err = abs(math.exp(x) - e_approx)
    while Err > threshold:
        n+=1
        e_approx = Taylor(x, n)
        Err = abs(math.exp(x) - e_approx)
        if Err < threshold:
            print(e_approx, math.exp(x))

err_e(8, 0.0001)