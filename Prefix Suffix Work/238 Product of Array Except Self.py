"""
238 Product of Array Except Self
* Problem: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
* Algorithm: Use prefix, suffix array
result[i] = left[i-1]*right[i+1]
where left[i-1] = input[0]*input[1]* ... * input[i-1]
      right[i+1] = input[i+1]*input[i+2]* ... * input[n-1]
left[i] = input[i]*left[i-1]
right[i] = input[i]*right[i+1]
* Time-complexity: O(3n) = O(n)
* Space-complexity: O(3n) = O(n)
"""
def productExceptSelf(nums):
    n = len(nums)
    left = [1 for i in range(n)]
    left[0] = nums[0]
    right = [None for i in range(n)]
    right[n-1] = nums[n-1]
    result = [1 for i in range(n)]
    for i in range(1, n):
        left[i] = nums[i]*left[i-1]
        right[n-i-1] = nums[n-i-1]*right[n-i]
    for i in range(1, n-1):
        result[i] = left[i-1]*right[i+1]
    result[0] = right[1]
    result[n-1] = left[n-2]
    return result

