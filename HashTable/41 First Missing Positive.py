"""
* Problem: 41. First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer. You must implement an algorithm
that runs in O(n) time and uses constant extra space.
Example 1: Input: nums = [1,2,0] -> Output: 3
Example 2: Input: nums = [3,4,-1,1] -> Output: 2
Example 3: Input: nums = [7,8,9,11,12] -> Output: 1
* Algorithm:
All numbers that are negative or greater than n should be ignored because they cannot be the smallest missing pos int.
- HashTable with O(n) auxiliary space
Create a hashtable h of size n, the keys are the elements of nums, values are True if the element is positive and <= n,
False otherwise. The hashtable here can be an array, so the hashtable's key is the index of the array's elements.
Accessing elements of an array through its index is O(1).
Try from 1 to n if a number is in the hashtable: the first number NOT in the hashtable is the smallest missing positive.
- Use the input array as the hashtable so the auxiliary space become O(1)
If nums[i] = j and 1<= j <= n, then the hashtable need to have key=j,value=True. Since we use the input array as the
hashtable with array index as key, we need to store True/False value. If we set nums[j] = True then we lose the value
nums[j]. A trick to combine storing True value for nums[j] and at the same time store nums[j] is: flip the sign of
nums[j].
- Algorithm: use the input array
+ Set nums[i] = 1 if nums[i] < 0 or nums[i] > n
+ Set when nums[i] = j and 1 <= j <= n, set nums[j] = -nums[j], i.e. flip the sign of nums[j]
+ The first positive element in nums is the missing positive number
+ Since we use 1, we need to chek if 1 can be the missing positive number first.
* Time-complexity: O(n)
* Space-complexity: O(1)
"""
def firstMissingPositive(nums):
    n = len(nums)
    contains1 = False
    for i in range(n):
        if nums[i] == 1:
            contains1 = True
            # nums[0], nums[i] = nums[i], nums[0]
            break
    if not contains1:
        return 1
    for i in range(n):
        if nums[i] <= 1 or nums[i] > n:
            nums[i] = 1
    print(nums)
    nth_element = 1
    for i in range(n):
        abs_value_i = abs(nums[i])
        if abs(nums[i]) == n:
            nums[0] = -n
        else:
            if nums[abs_value_i] >= 1:
                nums[abs_value_i] = -nums[abs_value_i]
    print(nums)
    result = None
    for i in range(1, n):
        if nums[i] > 0:
            result = i
            break
    if result is None:
        if nums[0] == -n:
            return n+1
        else:
            return n
    else:
        return result

a = [3,4,-1,1]
a = [1, 2, 0]
a = [3,4,-1,1]
print(firstMissingPositive(a))

