from branch_and_bound_v2 import Bound, Constraint, BranchAndBoundSolver
from dynamic_programming import *
import matplotlib.pyplot as plt

class Simulator:
    def simulate(self):
        sim_times_bb = self.simulate_bb()
        sim_times_dp = self.simulate_dp()

        plt.plot(sim_times_bb, label="Branch and Bound")
        plt.plot(sim_times_dp, label="Dynamic Programming")
        plt.ylabel("Simulation Time (s)")
        plt.xlabel("Number of Items")
        plt.title("Number of Items vs Simulation Time")
        plt.legend(loc="upper left")
        plt.show()

    def simulate_bb(self):
        # Datasets from https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
        file_sets = [
            ["p02_p.txt", "p02_w.txt", "p02_c.txt", "p02_s.txt"], # 5 weights with capacity of 26
            ["p03_p.txt", "p03_w.txt", "p03_c.txt", "p03_s.txt"], # 6 weights with capacity of 190
            ["p04_p.txt", "p04_w.txt", "p04_c.txt", "p04_s.txt"], # 7 weights with capacity of 50
            ["p06_p.txt", "p06_w.txt", "p06_c.txt", "p06_s.txt"], # 7 weights with capacity of 169
            ["p05_p.txt", "p05_w.txt", "p05_c.txt", "p05_s.txt"], # 8 weights with capacity of 104
            ["p01_p.txt", "p01_w.txt", "p01_c.txt", "p01_s.txt"], # 10 weights with capacity of 165
            ["p07_p.txt", "p07_w.txt", "p07_c.txt", "p07_s.txt"], # 15 weights with capacity of 750
            ["p08_p.txt", "p08_w.txt", "p08_c.txt", "p08_s.txt"], # 24 weights with capacity of 6404180
        ]

        sim_times = []
        branch_counter = []

        for file_set in file_sets:
            obj = []
            lhs = []
            bounds = []
            rhs = None
            opt_weights =[]

            start_time = time.time()

            for (idx, file_name) in enumerate(file_set):
                file1 = open(file_name)
                count = 0

                while True:
                    count += 1

                    # Get next line from file
                    line = file1.readline()

                    # If line is empty end of file reached
                    if not line:
                        break

                    if idx == 0:
                        obj.append(-1 * int(line.strip()))
                        bounds.append(Bound(0, 1))
                    elif idx == 1:
                        lhs.append(int(line.strip()))
                    elif idx == 2:
                        rhs = int(line.strip())
                    else:
                        opt_weights.append(int(line.strip()))
            
            bb = BranchAndBoundSolver(obj, [Constraint(lhs, rhs)], bounds, zero_one=True)
            opt = bb.solve()
            
            for (idx, w) in enumerate(opt[1]):
                assert(opt_weights[idx] == w)
            
            sim_times.append(time.time() - start_time)
            branch_counter.append(opt[2])

            print("--- %s seconds ---" % (time.time() - start_time))
            print("Branching: ", opt[2])
        
        return sim_times

    def simulate_dp(self):
        # Datasets from https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
        file_sets = [
            ["p02_p.txt", "p02_w.txt", "p02_c.txt", "p02_s.txt"], # 5 weights with capacity of 26
            ["p03_p.txt", "p03_w.txt", "p03_c.txt", "p03_s.txt"], # 6 weights with capacity of 190
            ["p04_p.txt", "p04_w.txt", "p04_c.txt", "p04_s.txt"], # 7 weights with capacity of 50
            ["p06_p.txt", "p06_w.txt", "p06_c.txt", "p06_s.txt"], # 7 weights with capacity of 169
            ["p05_p.txt", "p05_w.txt", "p05_c.txt", "p05_s.txt"], # 8 weights with capacity of 104
            ["p01_p.txt", "p01_w.txt", "p01_c.txt", "p01_s.txt"], # 10 weights with capacity of 165
            ["p07_p.txt", "p07_w.txt", "p07_c.txt", "p07_s.txt"], # 15 weights with capacity of 750
            ["p08_p.txt", "p08_w.txt", "p08_c.txt", "p08_s.txt"], # 24 weights with capacity of 6404180
        ]

        sim_times = []

        for file_set in file_sets:
            W = None
            val = []
            wt = []

            start_time = time.time()

            for (idx, file_name) in enumerate(file_set):
                file1 = open(file_name)
                count = 0

                while True:
                    count += 1

                    # Get next line from file
                    line = file1.readline()

                    # If line is empty end of file reached
                    if not line:
                        break

                    if idx == 0:
                        val.append(int(line.strip()))
                    elif idx == 1:
                        wt.append(int(line.strip()))
                    elif idx == 2:
                        W = int(line.strip())
            
            opt = knapSack(W, wt, val, len(val))
            print(opt)
            
            sim_times.append(time.time() - start_time)
            print("--- %s seconds ---" % (time.time() - start_time))
        
        return sim_times

sim = Simulator()
sim.simulate()