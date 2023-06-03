import sympy as sp
import math as math

"""
2/6/2023
Newton Raphson's method, to approximate a function
Kahyberth Stiven Gonzalez Sayas: 2060121-3743
"""
# fx = function, xi = starting point, apx = approximation with exact figures
def newtonRaphson(fx,xi, apx = None):
    x = sp.Symbol('x')
    fx = sp.sympify(fx)
    dx = sp.diff(fx,x)
    x1 = xi + 1
    x1_n = [1]
    c = 0
    while (True):
        c+=1
        x1 = x1 - (math.fabs(fx.subs(x,x1))/math.fabs(dx.subs(x,x1)))
        if ( x1 == x1_n[-1] or c == apx ):
            print(x1) # Final root value
            break
        x1_n.append(x1) # 1.5, 1.34782, 1.32520, 1.324718, 1324746
    return x1_n; #History of all drifts

#TEST
dato = newtonRaphson('x**3-x-1',1)
for i in range(1, len(dato)):
    print("History of all drifts: ", dato[i])

