from sympy import *

x, y = symbols('x y')
f =   2*y+x + 1
g = Rational(3,2)*pi + exp(I*x) / (x**2 + y)

# coeff(x, n): As you can see, it is for finding the coefficient of "variables" in mathematical expressions.
# So if you want to get the constant, `coeff` is not the method you're looking for

# # Method 1: A bit comlicated to use M. 1
# expr_f = Poly(f)  # Or you can do it explcitly expr = Poly(f, x, y)
# expr_g = Poly(g, exp(I*x), 1/(x**2 + y)) # Need to hard code the variable when the expression is getting more complex
# coeffs_f = expr_f.coeffs()
# coeffs_g = expr_g.coeffs()
# print(coeffs_f)  # [1, 2, 1]
# print(coeffs_g)  # [1, 3*pi/2]

# Method 2: This one is preferable, since you don't need to hard code the Poly expression
get_const = lambda expr: expr.func(*[var for var in expr.args if not var.free_symbols])
const_f = get_const(f)
const_g = get_const(g)
print(const_f)  # 1
print(const_g)  # 3*pi/2