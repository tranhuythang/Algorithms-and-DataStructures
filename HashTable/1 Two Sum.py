def twoSum(arr, sum):
    """
    1. Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    :param arr:
    :param sum:
    :return:
    """
    map = {}
    complement = 0    
    for i in range(len(arr)):
        complement = sum - arr[i]
        if complement in map:
            return i, map[complement]
        else:
            map[arr[i]] = i
    return "Not Found" 

arr = [1, 2, 4, 5, 7, 9, 0, 11]
sum = 9
print(twoSum(arr, sum))


