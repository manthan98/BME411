import math
from scipy.optimize import linprog

class Constraint:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

class Bound:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

class Node:
    def __init__(self, f_opt, opt, feasible, bounds):
        self.f_opt = f_opt
        self.opt = opt
        self.feasible = feasible
        self.bounds = bounds

class BranchAndBoundSolver:
    def __init__(self, obj, constraints, bounds):
        self.obj = obj
        self.constraints = constraints
        self.bounds = bounds
    
    def solve(self):
        root = Node(float('-inf'), [], False, self.bounds)
        self.lp_solve(root)
        
        if root.feasible:
            return root.f_opt
        
        queue = []
        incumbent = float('-inf')
        self.branch(root, queue)

        while len(queue) > 0:
            node = queue.pop(0)
            self.lp_solve(node)

            if node.f_opt == float('-inf'):
                print("Infeasible")
                continue

            if node.f_opt <= incumbent:
                print("Pruning...")
            elif node.f_opt > incumbent and node.feasible:
                incumbent = node.f_opt
            elif node.f_opt > incumbent and not node.feasible:
                print("Branching...")
                self.branch(node, queue)
        
        return incumbent
    
    def lp_solve(self, node):
        lhs_ineq = []
        rhs_ineq = []
        for constraint in self.constraints:
            lhs_ineq.append(constraint.lhs)
            rhs_ineq.append(constraint.rhs)
        
        bnd = []
        for bound in node.bounds:
            bnd.append((bound.lower, bound.upper))
        
        print(lhs_ineq, rhs_ineq, bnd)
        opt = linprog(c=self.obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
        if not opt.success:
            return
        
        node.f_opt = -1 * opt.fun
        node.opt = opt.x.tolist()
        print(opt)

        feasible = True
        for x in opt.x:
            if not x.is_integer():
                feasible = False
        node.feasible = feasible
    
    def branch(self, node, queue):
        x = [x for x in node.opt if not x.is_integer()]
        largest_x = max(x)
        largest_x_idx = node.opt.index(largest_x)
        print(x, largest_x, largest_x_idx)

        bounds = []
        for idx, bound in enumerate(node.bounds):
            if idx == largest_x_idx:
                bounds.append(Bound(0, math.floor(largest_x)))
            else:
                bounds.append(bound)

        left_node = Node(float('-inf'), [], False, bounds)
        queue.append(left_node)

        bounds = []
        for idx, bound in enumerate(node.bounds):
            if idx == largest_x_idx:
                bounds.append(Bound(math.ceil(largest_x), float('inf')))
            else:
                bounds.append(bound)

        right_node = Node(float('-inf'), [], False, bounds)
        queue.append(right_node)

def lp_test():
    obj = [-3, -4]
    lhs_ineq = [[7, 11], [3, -1]]
    rhs_ineq = [88, 12]
    bnd = [(0, float('inf')), (0, float('inf'))]
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
    print(opt)

# Driver code
obj = [-3, -4]
constraints = [
    Constraint([7, 11], 88),
    Constraint([3, -1], 12)
]
bounds = [
    Bound(0, float('inf')),
    Bound(0, float('inf'))
]

# obj = [-100, -150]
# constraints = [
#     Constraint([8000, 4000], 40000),
#     Constraint([15, 30], 200)
# ]
# bounds = [
#     Bound(0, float('inf')),
#     Bound(0, float('inf'))
# ]

# obj = [-24, -2, -20, -4]
# constraints = [
#     Constraint([8, 1, 5, 4], 9)
# ]
# bounds = [
#     Bound(0, 1),
#     Bound(0, 1),
#     Bound(0, 1),
#     Bound(0, 1)
# ]

bb = BranchAndBoundSolver(obj, constraints, bounds)
opt = bb.solve()
print(opt)