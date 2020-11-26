import math
import time
import matplotlib.pyplot as plt
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
    def __init__(self, obj, constraints, bounds, zero_one=False):
        self.obj = obj
        self.constraints = constraints
        self.bounds = bounds
        self.zero_one = zero_one
    
    def solve(self):
        root = Node(float('-inf'), [], False, self.bounds)
        self.lp_solve(root)
        
        if root.feasible:
            return root.f_opt
        
        queue = []
        incumbent = float('-inf')
        incumbent_opt = []
        self.branch(root, queue)

        branch_counter = 0

        while len(queue) > 0:
            node = queue.pop(0)
            self.lp_solve(node)

            if node.f_opt == float('-inf'):
                # print("Infeasible")
                continue

            # if node.f_opt <= incumbent:
            #     print("Pruning...")
            if node.f_opt > incumbent and node.feasible:
                incumbent = node.f_opt
                incumbent_opt = node.opt
            elif node.f_opt > incumbent and not node.feasible:
                # print("Branching...")
                self.branch(node, queue)
                branch_counter += 1
        
        return (incumbent, incumbent_opt, branch_counter)
    
    def lp_solve(self, node):
        lhs_ineq = []
        rhs_ineq = []
        for constraint in self.constraints:
            lhs_ineq.append(constraint.lhs)
            rhs_ineq.append(constraint.rhs)
        
        bnd = []
        for bound in node.bounds:
            bnd.append((bound.lower, bound.upper))
        
        # print(lhs_ineq, rhs_ineq, bnd)
        opt = linprog(c=self.obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
        if not opt.success:
            return
        
        node.f_opt = -1 * opt.fun
        node.opt = opt.x.tolist()
        # print(node.opt)

        feasible = True
        for x in opt.x:
            if not x.is_integer():
                feasible = False
        node.feasible = feasible
    
    def branch(self, node, queue):
        x = [x for x in node.opt if not x.is_integer()]
        largest_x = max(x)
        largest_x_idx = node.opt.index(largest_x)

        bounds = []
        for idx, bound in enumerate(node.bounds):
            if idx == largest_x_idx:
                if self.zero_one:
                    bounds.append(Bound(0, 0))
                else:
                    bounds.append(Bound(0, math.floor(largest_x)))
            else:
                bounds.append(bound)

        left_node = Node(float('-inf'), [], False, bounds)
        queue.append(left_node)

        bounds = []
        for idx, bound in enumerate(node.bounds):
            if idx == largest_x_idx:
                if self.zero_one:
                    bounds.append(Bound(1, 1))
                else:
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

# def simulate():
#     # Datasets from https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
#     file_sets = [
#         ["p02_p.txt", "p02_w.txt", "p02_c.txt", "p02_s.txt"], # 5 weights with capacity of 26
#         ["p03_p.txt", "p03_w.txt", "p03_c.txt", "p03_s.txt"], # 6 weights with capacity of 190
#         ["p04_p.txt", "p04_w.txt", "p04_c.txt", "p04_s.txt"], # 7 weights with capacity of 50
#         ["p06_p.txt", "p06_w.txt", "p06_c.txt", "p06_s.txt"], # 7 weights with capacity of 169
#         ["p05_p.txt", "p05_w.txt", "p05_c.txt", "p05_s.txt"], # 8 weights with capacity of 104
#         ["p01_p.txt", "p01_w.txt", "p01_c.txt", "p01_s.txt"], # 10 weights with capacity of 165
#         ["p07_p.txt", "p07_w.txt", "p07_c.txt", "p07_s.txt"], # 15 weights with capacity of 750
#         ["p08_p.txt", "p08_w.txt", "p08_c.txt", "p08_s.txt"], # 24 weights with capacity of 6404180
#     ]

#     sim_times = []
#     branch_counter = []

#     for file_set in file_sets:
#         obj = []
#         lhs = []
#         bounds = []
#         rhs = None
#         opt_weights =[]

#         start_time = time.time()

#         for (idx, file_name) in enumerate(file_set):
#             file1 = open(file_name)
#             count = 0

#             while True:
#                 count += 1

#                 # Get next line from file
#                 line = file1.readline()

#                 # If line is empty end of file reached
#                 if not line:
#                     break

#                 if idx == 0:
#                     obj.append(-1 * int(line.strip()))
#                     bounds.append(Bound(0, 1))
#                 elif idx == 1:
#                     lhs.append(int(line.strip()))
#                 elif idx == 2:
#                     rhs = int(line.strip())
#                 else:
#                     opt_weights.append(int(line.strip()))
        
#         bb = BranchAndBoundSolver(obj, [Constraint(lhs, rhs)], bounds, zero_one=True)
#         opt = bb.solve()
        
#         for (idx, w) in enumerate(opt[1]):
#             assert(opt_weights[idx] == w)
        
#         sim_times.append(time.time() - start_time)
#         branch_counter.append(opt[2])

#         print("--- %s seconds ---" % (time.time() - start_time))
#         print("Branching: ", opt[2])
    
#     plt.plot(sim_times)
#     plt.ylabel("Simulation Time (s)")
#     plt.xlabel("Number of Items")
#     plt.title("Number of Items vs Simulation Time")
#     plt.show()

#     plt.plot(branch_counter)
#     plt.ylabel("Number of Branches")
#     plt.xlabel("Number of Items")
#     plt.title("Number of Items vs Branching")
#     plt.show()

# Driver code
# obj = [-3, -4]
# constraints = [
#     Constraint([7, 11], 88),
#     Constraint([3, -1], 12)
# ]
# bounds = [
#     Bound(0, float('inf')),
#     Bound(0, float('inf'))
# ]

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

# obj = [-20, -30, -10, -40]
# constraints = [
#     Constraint([2, 4, 3, 7], 10),
#     Constraint([10, 7, 20, 15], 40),
#     Constraint([1, 10, 1, 0], 10)
# ]
# bounds = [
#     Bound(0, 1),
#     Bound(0, 1),
#     Bound(0, 1),
#     Bound(0, 1)
# ]

# obj = [-300, -90, -400, -150]
# constraints = [
#     Constraint([35000, 10000, 25000, 90000], 120000),
#     Constraint([4, 2, 7, 3], 12),
#     Constraint([1, 1, 0, 0], 1)
# ]
# bounds = [
#     Bound(0, 1),
#     Bound(0, 1),
#     Bound(0, 1),
#     Bound(0, 1)
# ]

# bb = BranchAndBoundSolver(obj, constraints, bounds)
# opt = bb.solve()
# print(opt)

# simulate()
