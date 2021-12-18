"""
*Problem: You are given an integer array nums of length n which represents a permutation of all the integers in the
range [0, n - 1].
The number of global inversions is the number of the different pairs (i, j) where: 0 <= i < j < n; nums[i] > nums[j]
The number of local inversions is the number of indices i where: 0 <= i < n – 1; nums[i] > nums[i + 1]
Return true if the number of global inversions is equal to the number of local inversions.
*Algorithm: Note that a local inversion is also a global inversion, so number of global inversions is always > number of
local inversion.
a[i] has a global but not local inversion if min(a[i+2], ..., a[n-1]) < a[i].
*Time-complexity: O(n)
*Space-complexity: O(1). Don't need to store all min(a[i+2], ..., a[n-1]) for all i
"""
def GlobalLocalInversion(nums):
    n = len(nums)
    if n <= 2:
        return True

    min_suffix = nums[n - 1]
    for i in range(n - 3, -1, -1):
        if nums[i] > min_suffix:
            return False
        else:
            min_suffix = min(min_suffix, nums[i + 1])
    return True


