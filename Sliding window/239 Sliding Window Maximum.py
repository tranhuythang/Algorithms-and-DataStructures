"""
* Problem: You are given an array of integers nums, there is a sliding window of size k which is moving from the very
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves
right by one position. Return the max of all sliding windows.
Example: Input: nums = [1,3,-1,-3,5,3,6,7], k = 3 -> Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

* Algorithm: Brute force takes O(nk) where n = array size, k = window size. The following algorithm is O(n) algorithm.
Using sliding window: calculate max of the first sliding window: max(a[0, ..., k-1]). However the max of the next
sliding window max(a[1, ..., k]) cannot be calculated in O(1) from max(a[0, ..., k-1]).

https://leetcode.com/problems/sliding-window-maximum/
"""
def maxSlidingWindow(nums, k):
    print('input', nums)
    n = len(nums)
    if k == 1:
        return nums

    result = [None for i in range(n-k+1)]

    left = [None for i in range(n)]
    left[0] = nums[0]
    right = [None for i in range(n)]
    right[n-1] = nums[n-1]

    for i in range(n-2, -1, -1):
        if i % k == k-1:
            right[i] = nums[i]
        else:
            right[i] = max(right[i+1], nums[i])
    print('right', right)

    for i in range(1, n):
        if i % k == 0:
            left[i] = nums[i]
        else:
            left[i] = max(left[i-1], nums[i])
    print('left ', left)

    for i in range(n-k+1):
        result[i] = max(right[i], left[i+k-1])
    return result

input = [[[1,3,-1,-3,5,3,6,7], 3]]
for s in input:
    print(maxSlidingWindow(s[0], s[1]))