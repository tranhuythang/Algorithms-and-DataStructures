"""
* Problem: 1762. Buildings With an Ocean View
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the
buildings in the line. The ocean is to the right of the buildings. A building has an ocean view if the building can see
the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller
height. Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
Example: Input: heights = [4,2,3,1] -> Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
* Algorithm:
Solution 1: set height_max = heights[-1]. Loop from the right, if heights[i] > height_max, update height_max = heights[i]
and record i.
Solution 2: Loop from the left and use stack. If heights[i] >= the top stack, pop the stack until heights[i] < the top
stack; at this point push heights[i] into the stack
* Time complexity: O(n)
* Space complexity: O(n)
"""
# Solution 1: Using Stack

import collections
# def findBuildings(heights):
#     stack = collections.deque()
#     for i in range(len(heights)):
#         while len(stack) > 0 and heights[i] >= heights[stack[-1]]:
#             stack.pop()
#         stack.append(i)
#     return list(stack)

# Solution 2:
def findBuildings(heights):
    n = len(heights)
    if n == 1:
        return [0]
    result = [n-1]
    heights_max = heights[-1]
    for i in range(n-1, -1, -1):
        if heights[i] > heights_max:
            result.append(i)
            heights_max = heights[i]
    return result[::-1]

a = [4, 2, 3, 1]
print(findBuildings(a))