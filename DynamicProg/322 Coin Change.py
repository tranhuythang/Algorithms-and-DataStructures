"""
* Problem: 322. Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a
total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money
cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Example 1: Input: coins = [1,2,5], amount = 11 -> Output: 3. Explanation: 11 = 5 + 5 + 1
Example 2: Input: coins = [2], amount = 3 -> Output: -1
* Algorithm: Dynamic Programming
Let result[n] be the minimum number of coins for exchange for amount of n.
result[0] = 0, result[1] = -1 if there is no 1 in coins[] or 1
result[k] = 1 + min{result[k - j]: k >= j and j in coins[]}
* Time-complexity: O(n)
* Space-complexity: O(n)
"""
def coinChange(coins, amount):
    n = len(coins)
    result = [-1 for i in range(amount+1)]
    result[0] = 0
    if amount == 0:
        return 0
    if 1 in coins:
        result[1] = 1
    else:
        result[1] = -1
    for i in range(2, amount+1):
        temp_min = float("inf")
        for j in coins:
            if (j <= i) and (result[i-j] != -1):
                if temp_min >= (result[i-j] + 1):
                    temp_min = result[i-j] + 1
        if temp_min == float("inf"):
            result[i] = -1
        else:
            result[i] = temp_min
    print(result)
    return result[amount]

print(coinChange([1, 2, 5], 11))