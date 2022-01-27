"""
* Problem: 1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
* Algorithm: Two Pointers
Use start, end for the begining and ending position of a windows of 1
Increase end, whenever it hits 0, increase zeros (the number of zeros).
When zeros > k, increase start.
    for end in range(n):
        if nums[end] == 0:
            zeros += 1
        while zeros > k and start <= end:
            if nums[start] == 0:
                zeros -= 1
            start += 1
        max_ones = max(max_ones, end - start + 1)
* Time-Complexity: O(2n)
end runs from 0 to n. In the worst case, start runs from 0 to n, so the total is O(2n) = O(n)
* Space-Complexity: O(1) since use only zeros, start, end
"""
def longestOne_SlideWindow(nums, k):
    n = len(nums)
    zeros = 0
    start = 0
    max_ones = 0
    for end in range(n):
        if nums[end] == 0:
            zeros += 1
        while zeros > k and start <= end:
            if nums[start] == 0:
                zeros -= 1
            start += 1
        max_ones = max(max_ones, end - start + 1)
    return max_ones


def longestOnes_DynamicProgram(nums, k):
    n = len(nums)
    one = []
    if nums[0] == 0:
        one.append(0)
    zero = []
    i = 0
    while i < n:
        j = 1
        while i+j < n and nums[i+j] == nums[i]:
            j += 1
        if nums[i] == 0:
            zero.append(j)
        else:
            one.append(j)
        i += j

    len_0 = len(zero)
    len_1 = len(one)
    if len_1 == len_0:
        one.append(0)

    L = [[0 for j in range(k+1)] for i in range(len_1)]
    for j in range(k+1):
        L[0][j] = one[0]
    for i in range(1, len_1):
        for j in range(k+1):
            if zero[i-1] <= j:
                L[i][j] = L[i-1][j-zero[i-1]] + zero[i-1] + one[i]
            else:
                L[i][j] = one[i] + j
    return max([L[i][k] for i in range(len_1)])

# def longestOnes_SlowWindow(nums, k):
#     n = len(nums)
#     one_block = []
#     zero_block = []
#     if nums[0] == 0:
#         one_block.append([0, 0])
#     zero_count = 0
#     i = 0
#     j = 0
#     while i < n:
#         j = 1
#         while i+j < n and nums[i+j] == nums[i]:
#             j += 1
#         if nums[i] == 1:
#             one_block.append([i, j])
#         else:
#             zero_block.append([i, j])
#             zero_count += j
#         i += j
#
#     if len(zero_block) == len(one_block):
#         one_block.append([len(one_block), 0])
#
#     # print('zero_count = ', zero_count)
#     if k >= zero_count:
#         return n
#
#     if k == 0:
#         return max(map(lambda x:x[1], one_block))
#     # print('one_block = ', one_block)
#     # print('zero_block = ', zero_block)
#
#     zero_bit = []
#     for i in range(len(zero_block)):
#         # print('zero_bit = ', zero_bit)
#         j = zero_block[i][1]
#         if j == 1:
#             zero_bit.append([zero_block[i][0], one_block[i][1], one_block[i+1][1]])
#         else:
#             zero_bit.append([zero_block[i][0], one_block[i][1], 0])
#             for l in range(1, j-1):
#                 zero_bit.append([zero_block[i][0] + l, 0, 0])
#             zero_bit.append([zero_block[i][0] + j-1, 0, one_block[i+1][1]])
#
#     # print('zero_bit = ', zero_bit)
#
#     current_one_count = 0
#     for i in range(k):
#         current_one_count += zero_bit[i][1]
#     current_one_count += zero_bit[k-1][2]
#     # print('current_one_count = ', current_one_count)
#     max_one_count = current_one_count
#
#     for j in range(0, len(zero_bit)-k):
#         current_one_count = current_one_count - zero_bit[j][1] + zero_bit[j+k][2]
#         # print('current_one_count = ', current_one_count)
#         if max_one_count < current_one_count:
#             max_one_count = current_one_count
#
#     return max_one_count+k



a = [[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1], 3]
# a = [[1,1,1,0,0,0,1,1,1,1,0], 2]
# a = [[0,0,1,1,1,0,0], 0]
a = [[0,0,0,0], 0]

print(longestOne_SlideWindow(a[0], a[1]))



