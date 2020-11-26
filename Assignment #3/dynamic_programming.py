# Adapted from https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# A naive recursive implementation of 0-1 Knapsack Problem using Dynamic Programming.

import math
import time
import matplotlib.pyplot as plt

def knapSack(W, wt, val, n):
    # Base Case 
    if n == 0 or W == 0: 
        return 0
  
    # If weight of the nth item is 
    # more than Knapsack of capacity W, 
    # then this item cannot be included 
    # in the optimal solution 
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))