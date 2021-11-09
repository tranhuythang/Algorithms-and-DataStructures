"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def climbStair_memoization(n):
    result = {}
    result[1] = 1
    result[2] = 2
    def wayCount(n):
        if n in result:
            return result[n]
        else:
            result[n] = wayCount(n-1) + wayCount(n-2)
            return result[n]
    return wayCount(n)

def climbStair_tabulation(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    result = [0 for i in range(n)]
    result[0] = 1
    result[1] = 2
    for i in range(n-2):
        result[i+2] = result[i+1] + result[i]
    return result[n-1]

test = [1, 2, 3, 4, 5, 6, 7]
for n in test:
    print(n, '->', climbStair_memoization(n), climbStair_tabulation(n))
