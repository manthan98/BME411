from branch_and_bound import Constraint, Bound, BranchAndBoundSolver

# Sample problems (of varying levels of complexity) to test the Branch and Bound solver.

obj = [-3, -4]
constraints = [
    Constraint([7, 11], 88),
    Constraint([3, -1], 12)
]
bounds = [
    Bound(0, float('inf')),
    Bound(0, float('inf'))
]

print("\nProblem #1: max f(X) = 3x1 + 4x2 subject to 7x1 + 11x2 <= 88 and 3x1 - x2 <= 12")
bb = BranchAndBoundSolver(obj, constraints, bounds)
opt = bb.solve()
print(f"Optimal solution: {opt[0]}, optimal points: {opt[1]}\n")

obj = [-100, -150]
constraints = [
    Constraint([8000, 4000], 40000),
    Constraint([15, 30], 200)
]
bounds = [
    Bound(0, float('inf')),
    Bound(0, float('inf'))
]

print("Problem #2: max f(X) = 100x1 + 150x2 subject to 8000x1 + 4000x2 <= 40000 and 15x1 + 30x2 <= 200")
bb = BranchAndBoundSolver(obj, constraints, bounds)
opt = bb.solve()
print(f"Optimal solution: {opt[0]}, optimal points: {opt[1]}\n")

obj = [-24, -2, -20, -4]
constraints = [
    Constraint([8, 1, 5, 4], 9)
]
bounds = [
    Bound(0, 1),
    Bound(0, 1),
    Bound(0, 1),
    Bound(0, 1)
]

print("Problem #3: max f(X) = 24x1 + 2x2 + 20x3 + 4x4 subject to 8x1 + x2 + 5x3 + 5x4 <= 9 and x1, x2, x3, x4 E [0, 1]")
bb = BranchAndBoundSolver(obj, constraints, bounds)
opt = bb.solve()
print(f"Optimal solution: {opt[0]}, optimal points: {opt[1]}\n")

obj = [-20, -30, -10, -40]
constraints = [
    Constraint([2, 4, 3, 7], 10),
    Constraint([10, 7, 20, 15], 40),
    Constraint([1, 10, 1, 0], 10)
]
bounds = [
    Bound(0, 1),
    Bound(0, 1),
    Bound(0, 1),
    Bound(0, 1)
]

print("Problem #4: max f(X) = 20x1 + 30x2 + 10x3 + 40x4 subject to 2x1 + 4x2 + 3x3 + 7x4 <= 10, 10x1 + 7x2 + 20x3 + 15x4 <= 40, x1 + 10x2 + x3 <= 10 and x1, x2, x3, x4 E [0, 1]")
bb = BranchAndBoundSolver(obj, constraints, bounds)
opt = bb.solve()
print(f"Optimal solution: {opt[0]}, optimal points: {opt[1]}\n")

obj = [-300, -90, -400, -150]
constraints = [
    Constraint([35000, 10000, 25000, 90000], 120000),
    Constraint([4, 2, 7, 3], 12),
    Constraint([1, 1, 0, 0], 1)
]
bounds = [
    Bound(0, 1),
    Bound(0, 1),
    Bound(0, 1),
    Bound(0, 1)
]

print("Problem #5: max f(X) = 300x1 + 90x2 + 400x3 + 150x4 subject to 35000x1 + 10000x2 + 25000x3 + 90000x4 <= 120000, 4x1 + 2x2 + 7x3 + 3x4 <= 12, x1 + x2 <= 1 and x1, x2, x3, x4 E [0, 1]")
bb = BranchAndBoundSolver(obj, constraints, bounds)
opt = bb.solve()
print(f"Optimal solution: {opt[0]}, optimal points: {opt[1]}\n")