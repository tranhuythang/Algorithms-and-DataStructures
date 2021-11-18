def bestTimeBuySell(prices):
    """
    121. Best Time to Buy and Sell Stock
    You are given an pricesay prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
    future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Dynamic Programming Solution:
    Let p[n] be the max profit (which can be negative) when selling at prices[n]
    p[1] = prices[1] - prices[0]
    p[n+1] = prices[n+1] - buy[n+1]
    where buy[n+1] = min(prices[n], buy[n])
          buy[n] = prices[n] - p[n]
    so p[n+1] = prices[n+1] - min(prices[n], prices[n] - p[n])
    """
    n = len(prices)
    p = [0 for i in range(n)]
    if n <= 1:
        return 0
    p[1] = prices[1] - prices[0]
    for k in range(1, n-1):
        p[k+1] = prices[k+1] - min(prices[k], prices[k] - p[k])
    return max(p)


test = [[7,1,5,3,6,4], [7,6,4,3,1], [1, 2, 3, 9, 7, 4, 8], [1, 2, 4, 8, 6, 5, 0, 9], [1, 2, 4, 8, 6, 5, 0, 2], [6, 4, 1, 0, -2], [2,1,2,1,0,1,2], [2,0,2,1,0,1,2]]
for s in test:
    print(s, '->', bestTimeBuySell(s))
