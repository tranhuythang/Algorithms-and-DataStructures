"""
*Problem: Given a non-decreasing sorted array of integers numbers[] and an integer k. Find two indices i, j so that
numbers[i] + numbers[j] == k; return [i+1, j+1] (assume the test works with 1-based indices so add 1 to your result).
Assume there is only one solution.
This problem can be solved by using HashMap with O(n) time, O(n) space and not using the array being sorted.
Use Two Pointers to solve this problem with O(n) time, O(1) space.
*Algorithm: Use two pointers i = 0 and j = n-1 and then increasing i, decreaing j until we get the result:
    while i < j:
        if numbers[i] + numbers[j] == target:
            return i, j as the result
        if numbers[i] + numbers[j] < target:
            increase i
        if numbers[i] + numbers[j] > target:
            decrease j
*Time-complexity: O(n)
*Space-complexity: O(1)
"""
def twoSum2(numbers, target):
    n = len(numbers)
    i = 0
    j = n-1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
