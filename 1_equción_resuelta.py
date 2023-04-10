from sympy import symbols, solve, Eq

x = symbols('x')
expr = 25 ** x -5
sol = solve(expr)

print(sol)