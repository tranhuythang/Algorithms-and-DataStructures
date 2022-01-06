"""
* Problem: You are given a sorted array consisting of only integers where every element appears exactly twice, except
for one element which appears exactly once. Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
* Algorithm:
The single element is the cut between two halves of the array:
left half: a[2k-1] < a[2k] = a[2k+1]
right half: a[2k-1] = a[2k] < a[2k+1]
so use binary search to find that element
* Time-complexity: log(n) since the array is sorted
* Space-complexity: O(1)
"""
def singleNonDuplicate(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]

    left = 0
    right = n-1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        else:
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid+1]:
                    right = mid
                else:
                    left = mid
    return nums[left]
