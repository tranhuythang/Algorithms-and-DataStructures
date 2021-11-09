def bestTimeBuySell(arr):
    """
    121. Best Time to Buy and Sell Stock
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
    future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    :param arr:
    :return:
    """
    p = [-1000 for i in range(len(arr))]
    p[1] = arr[0] - arr[1]
    buy = arr[0]
    maxProfit = - buy + arr[1]
    for n in range(1, len(arr) - 1):
        buy = min(buy, arr[n])
        p[n+1] = - buy + arr[n+1]
        maxProfit = max(maxProfit, p[n+1])
    return maxProfit

test = [[7,1,5,3,6,4], [7,6,4,3,1], [1, 2, 3, 9, 7, 4, 8], [1, 2, 4, 8, 6, 5, 0, 9], [1, 2, 4, 8, 6, 5, 0, 2], [6, 4, 1, 0, -2]]
for s in test:
    print(s, '->', bestTimeBuySell(s))
