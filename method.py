import sympy as sp
import math as math
def newtonRaphson(fx,xi,apx):
    x = sp.Symbol('x')
    fx = sp.sympify(fx)
    dx = sp.diff(fx,x)
    x1 = xi + 1
    cn = 0
    while (True):
        x1 = x1 - (math.fabs(fx.subs(x,x1))/math.fabs(dx.subs(x,x1)))
        print(x1)
        cn += 1
        if ( cn == apx ):
            break

#TEST
print(newtonRaphson('x**3-x-1',1,5))

