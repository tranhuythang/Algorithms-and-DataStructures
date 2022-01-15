"""
* Problem: 746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost,
you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
Example 1: Input: cost = [10,15,20] -> Output: 15
Explanation: You will start at index 1. Pay 15 and climb two steps to reach the top. The total cost is 15.
Example 2: Input: cost = [1,100,1,1,1,100,1,1,100,1] -> Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
* Algorithm: Dynamic Programming
Assume len(cost) = n.
Let result[k] (0-based index) be the minimum cost to be on the kth step, so the solution for the problem is result[n]
base case: set result[0] = result[1] = 0
recurrence: result[k+1] = min(result[k] + cost[k], result[k-1] + cost[k-1])
* Time-complexity: O(n)
* Space-complexity: O(n) can be reduced to O(1)
"""
def minCostClimbingStairs(cost):
    n = len(cost)
    result = [0 for i in range(n+1)]
    for k in range(2, n+1):
        result[k] = min(result[k-1] + cost[k-1], result[k-2] + cost[k-2]) # space: O(n) can be reduced to O(1)
    return result[n]