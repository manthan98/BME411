import math
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Data structure to model a design constraint. The model
# assumes a standard form inequality.
class Constraint:
    def __init__(self, lhs, rhs):
        """
        Initializer that requires:
        1. the contents of the left hand side of the constraint inequality
        2. the contents of the right hand side of the constraint inequality
        """
        self.lhs = lhs
        self.rhs = rhs

# Data structure to model a boundary condition for a design variable.
class Bound:
    def __init__(self, lower, upper):
        """
        Initializer that requires:
        1. lower bound for the design variable
        2. upper bound for the design variable
        """
        self.lower = lower
        self.upper = upper

# Data structure to model a problem instance.
class Node:
    def __init__(self, f_opt, opt, feasible, bounds):
        """
        Initializer that requires:
        1. optimal solution for problem
        2. optimal integer points for corresponding solution
        3. whether the solution is an integer feasible solution
        4. any pre-existing boundary conditions for the problem instance
        """
        self.f_opt = f_opt
        self.opt = opt
        self.feasible = feasible
        self.bounds = bounds

class BranchAndBoundSolver:
    def __init__(self, obj, constraints, bounds, zero_one=False):
        """
        Initializer that requires:
        1. an objective function (in maximization form)
        2. constraints
        3. bounds for all design variables
        """
        self.obj = obj
        self.constraints = constraints
        self.bounds = bounds
        self.zero_one = zero_one
    
    def solve(self):
        """
        Solves the problem instance using the Branch and Bound algorithm. 
        Returns the optimal solution and the corresponding integer points.
        """
        root = Node(float('-inf'), [], False, self.bounds)
        self.lp_solve(root)
        
        # If solving the original problem yields the optimal integer feasible 
        # solution, terminate.
        if root.feasible:
            return root.f_opt
        
        queue = []
        incumbent = float('-inf')
        incumbent_opt = []
        self.branch(root, queue)

        branch_counter = 0

        # Process the enumeration tree as long as there are active nodes.
        while len(queue) > 0:
            node = queue.pop(0)
            self.lp_solve(node)

            # If the solution to the subproblem is infeasible (due to 
            # problem constraints), terminate.
            if node.f_opt == float('-inf'):
                continue

            # Case 1: solution to subproblem is less than upper bound, prune the node.
            # Case 2: solution to subproblem is better than upper bound and integer feasible, update upper bound.
            # Case 3: solution to subproblem is better than upper bound but not integer feasible, apply branching.
            if node.f_opt > incumbent and node.feasible:
                incumbent = node.f_opt
                incumbent_opt = node.opt
            elif node.f_opt > incumbent and not node.feasible:
                self.branch(node, queue)
                branch_counter += 1
        
        return (incumbent, incumbent_opt, branch_counter)
    
    def lp_solve(self, node):
        """
        Solves a problem through LP relaxation of the constraints using Simplex method.
        """

        # Extract the design constraints and boundaries.
        lhs_ineq = []
        rhs_ineq = []
        for constraint in self.constraints:
            lhs_ineq.append(constraint.lhs)
            rhs_ineq.append(constraint.rhs)
        
        bnd = []
        for bound in node.bounds:
            bnd.append((bound.lower, bound.upper))
        
        # Solve the problem using Simplex.
        opt = linprog(c=self.obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
        if not opt.success:
            return
        
        # Update the problem (node) with optimal solution.
        node.f_opt = -1 * opt.fun

        # Update the problem (node) with optimal solution points (may be integer/non-integer).
        node.opt = opt.x.tolist()

        # Determine if the optimal solution is integer feasible, and update relevant problem (node) field.
        feasible = True
        for x in opt.x:
            if not x.is_integer():
                feasible = False
        node.feasible = feasible
    
    def branch(self, node, queue):
        """
        Applies branching to problem (node), and constructs corresponding subproblems (nodes), and inserts into the tree.
        """

        # Determine the largest, non-integral point, and its corresponding index.
        x = [x for x in node.opt if not x.is_integer()]
        largest_x = max(x)
        largest_x_idx = node.opt.index(largest_x)

        # Construct an upper bound for left subproblem (node).
        bounds = []
        for idx, bound in enumerate(node.bounds):
            if idx == largest_x_idx:
                if self.zero_one:
                    bounds.append(Bound(0, 0))
                else:
                    bounds.append(Bound(0, math.floor(largest_x)))
            else:
                bounds.append(bound)

        # Create subproblem (node) and attach to tree.
        left_node = Node(float('-inf'), [], False, bounds)
        queue.append(left_node)

        # Construct a lower bound for right subproblem (node).
        bounds = []
        for idx, bound in enumerate(node.bounds):
            if idx == largest_x_idx:
                if self.zero_one:
                    bounds.append(Bound(1, 1))
                else:
                    bounds.append(Bound(math.ceil(largest_x), float('inf')))
            else:
                bounds.append(bound)

        # Create subproblem (node) and attach to tree.
        right_node = Node(float('-inf'), [], False, bounds)
        queue.append(right_node)
