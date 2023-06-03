import sympy as sp
import math as math

"""
3/6/2023
Newton Raphson's method, to approximate a function
Kahyberth Stiven Gonzalez Sayas
"""
# fx = function, xi = starting point, apx = approximation with exact figures
def newtonRaphson(fx, xi, apx=0):
    x = sp.Symbol('x')
    dx = sp.diff(fx, x)
    fx_exp = sp.sympify(fx)
    x_n = [1]
    c = 0
    while True:
        if xi == x_n[-1] or (apx > 0 and c == apx):
            break
        x_n.append(xi)
        xi = xi - (fx_exp.subs(x, xi) / dx.subs(x, xi))
        c += 1
    return xi
dato = newtonRaphson('exp(x)-2+x**2', 0.5, 3)

#Testing
#f(x) = ln(x)-2, The root is between 7 and 8, xi = 8, apx = 2, result = 7.389015142227567
#f(x) = 'exp(x)-2+x**2', xi = 0.5, apx = 3, result = 0.537274449174110
print(dato)