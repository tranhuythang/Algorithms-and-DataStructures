def maxSubarray(arr):
    """
    53 Maximum Sum of Contiguous Subarray
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
    sum and return its sum.
    A subarray is a contiguous part of an array.

    :param arr:
    :return:
    """
    p = [0 for i in range(len(arr))]
    maxSubArraySum = p[0] = arr[0]
    for n in range(len(arr) - 1):
        p[n+1] = arr[n+1] + max(0, p[n])
        maxSubArraySum = max(p[n+1], maxSubArraySum)
    return maxSubArraySum

test = [[-2,1,-3,4,-1,2,1,-5,4], [5,4,-1,7,8], [1, 1, -7, 3, -1, 2]]
for s in test:
    print(s, '->', maxSubarray(s))