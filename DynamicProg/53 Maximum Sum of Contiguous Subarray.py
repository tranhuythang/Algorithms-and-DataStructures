def maxSubnumsay(nums):
    """
    53 Maximum Sum of Contiguous Subnumsay
    Given an integer numsay nums, find the contiguous subnumsay (containing at least one number) which has the largest
    sum and return its sum.
    A subnumsay is a contiguous part of an numsay.

    :param nums:
    :return:
    """
    p = [0 for i in range(len(nums))]
    maxSubnumsaySum = p[0] = nums[0]
    for n in range(len(nums) - 1):
        p[n+1] = nums[n+1] + max(0, p[n])
        maxSubnumsaySum = max(p[n+1], maxSubnumsaySum)
    return maxSubnumsaySum

test = [[-2,1,-3,4,-1,2,1,-5,4], [5,4,-1,7,8], [1, 1, -7, 3, -1, 2]]
for s in test:
    print(s, '->', maxSubnumsay(s))