from random import randint
from scipy.optimize import linprog

class Item:
    def __init__(self, value, weight, amount):
        self.value = value
        self.weight = weight
        self.amount = amount

class Node:
    def __init__(self, f_opt, feasible, items):
        self.f_opt = f_opt
        self.feasible = feasible
        self.items = items

def solve(items, max_weight):
    root = Node(float('-inf'), False, items)
    lp_solve(root, max_weight)
    if root.feasible:
        return root.f_opt
    
    incumbent = float('-inf')
    
    queue = []
    branch(root, queue)
    print(queue)

    while len(queue) > 0:
        node = queue.pop(0)
        lp_solve(node, max_weight)

        if node.f_opt <= incumbent:
            print("Pruning the node")
            # Nothing - prune the node
        elif node.f_opt > incumbent and node.feasible:
            print("Feasible!")
            incumbent = node.f_opt
        elif node.f_opt > incumbent and not node.feasible:
            print("Branching...")
            branch(node, queue)
    
    return incumbent

def lp_solve(node, max_weight):
    obj = []
    lhs_ineq = [[]]
    rhs_ineq = []
    bnd = []

    for item in node.items:
        obj.append(-1 * item.value)
        if item.amount != -1:
            bnd.append((item.amount, item.amount))
        else:
            bnd.append((0, 1))
        lhs_ineq[0].append(item.weight)
    
    rhs_ineq.append(max_weight)

    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
    if opt.success and opt.fun.is_integer():
        feasible = True
        for x in opt.x:
            if not x.is_integer():
                feasible = False
        node.feasible = feasible
    
    node.f_opt = -1 * opt.fun

def branch(node, queue):
    item_idx = -1
    for i in range(len(node.items)):
        if node.items[i].amount == -1:
            item_idx = i
            break
    
    if item_idx == -1:
        return
    
    node.items[item_idx].amount = 0
    left_node = Node(float('-inf'), False, node.items)

    node.items[item_idx].amount = 1
    right_node = Node(float('-inf'), False, node.items)

    queue.append(left_node)
    queue.append(right_node)


def test_lp():
    obj = [-24, -2, -20, -4]
    lhs_ineq = [[8, 1, 5, 4]]
    rhs_ineq = [9]
    bnd = [(0, 1), (0, 1), (0, 1), (0, 1)]
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="revised simplex")
    print(opt)

# Driver code
items = [
    Item(24, 8, -1),
    Item(2, 1, -1),
    Item(20, 5, -1),
    Item(4, 4, -1)
]
max_weight = 9
opt = solve(items, 9)
print(opt)
