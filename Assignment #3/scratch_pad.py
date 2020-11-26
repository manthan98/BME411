import math
from scipy.optimize import linprog

def lp_test():
    obj = [-12, -7]
    lhs_ineq = [[2, 1], [3, 4], [1, 0], [0, 1]]
    rhs_ineq = [5, 10, 2, 3]
    bnd = [(0, float('inf')), (0, float('inf'))]
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
    print(opt)

lp_test()