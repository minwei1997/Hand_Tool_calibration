import numpy as np
from sympy import *
from numpy.linalg import inv

# Assume the origin poit is (1,0,0)
# and 4 points are p1(3,0,0) p2(1,0,2) p3(1,2,0) p4(-1,0,0)
# set four point 
p1 = np.array([31,0,0])
p2 = np.array([1,0,2])
p3 = np.array([1,2,0])
p4 = np.array([-1,0,0])

# Radius
R = 10

# symbol define
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# define equations
f1 = (x-p1[0])**2 + (y-p1[1])**2 + (z-p1[2])**2 - R**2
f2 = (x-p2[0])**2 + (y-p2[1])**2 + (z-p2[2])**2 - R**2
f3 = (x-p3[0])**2 + (y-p3[1])**2 + (z-p3[2])**2 - R**2
f4 = (x-p4[0])**2 + (y-p4[1])**2 + (z-p4[2])**2 - R**2

# define a function which is use to get the constant term of a equation
get_const = lambda expr: expr.func(*[var for var in expr.args if not var.free_symbols])

# get 3 subtracted equations 
res_f1 = expand(f1-f2)
res_f2 = expand(f2-f3)
res_f3 = expand(f3-f4)

# show 3 equations for observation
for j in range(3):
    print(eval("res_f"+str(j+1)))

# Ax = b  (establish)
A = np.zeros(shape=(3,3))
b = np.zeros(shape=(3,1))
for i in range(3):
    A[i][0] = eval("res_f"+str(i+1)).coeff(x)
    A[i][1] = eval("res_f"+str(i+1)).coeff(y)
    A[i][2] = eval("res_f"+str(i+1)).coeff(z)
    const = get_const(eval("res_f"+str(i+1)))
    
    b[i][0] = -const    # negative because transposition of term


# solve by matrix multiply
ans = np.dot(inv(A),b)
print(ans)

# solve just by equations
ans = solve((res_f1,res_f2,res_f3), (x, y,z))
print(ans)