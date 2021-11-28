"""
Problem: Given an integer array nums, return the length of the longest strictly increasing subsequence. Note [3,6,2,7]
is a subsequence of the array [0,3,1,6,2,2,7].
Dynamic Algorithm: Let LIS[k] be the the longest increasing subsequence ending at input[k] then
LIS[0] = 1
LIS[k] = max(LIS[j]: input[j] < input[k] and j < k) for k from 1 to the length of input
Time-Complexity: O(n^2)
Space-Complexity: O(n)
"""
def LongestIncreasingSubsequence(nums):
    n = len(nums)
    LIS = [1 for i in range(n)]
    previous_index = [0 for i in range(n)]
    for k in range(1, n):
        for j in range(k):
            if nums[j] < nums[k] and LIS[k] < LIS[j]+1:
                LIS[k] = LIS[j] + 1
                previous_index[k] = j
    max_LIS_ending_index = -1
    max_LIS = 1
    for i in range(n):
        if LIS[i] > max_LIS:
            max_LIS = LIS[i]
            max_LIS_ending_index = i
    LIS_index = [max_LIS_ending_index]
    i = max_LIS_ending_index
    while LIS[i] > 1:
        i = previous_index[i]
        LIS_index.append(i)
    print([nums[i] for i in LIS_index[::-1]])
    return max_LIS

test = [[1,3,6,7,9,4,10,5,6]]
for t in test:
    print(LongestIncreasingSubsequence(t))