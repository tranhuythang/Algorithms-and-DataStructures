"""
* Problem: 42. Trapping Rain Water 
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1: Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] -> Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2: Input: height = [4,2,0,3,2,5] -> Output: 9
* Algorithm:

Approach 1: Stack
Push height[0] to a stack
for i in range(1, len(height)):
    if height[i] < stack.top: push height[i]
    if height[i] >= stack.top: pop stack.top and subtract the total_water by the height of the stack.top
    Note when len(stack) == 1 and height[i] > the height of this stack.top then calculate the water contained in those two heights
    subtracted by the height of element poped from the stack. The height[i] in this case becomes the first element in the stack 
    and we calculate the water from this height
The above process will result in a stack of decreasing height. By poping repeatedly stack.top, it's easy to calculate the result.

Approach 2: Slice the water VERTICALLY and calculate the sum of all slices (like integral calculation)
For each height, which is a slice: if this slice is contained by one height higher on the left, one height higher on the right then the slice
contributes to the total water. Assume left_max, right_max are the max of height on the left, right then the height contributes
min(left_max, right_max) if min(left_max, right_max) >= height, or 0 otherwise. 
The algorithm can be optimized by calculate an array of left_max[i], right_max[i]: the left_max, right_max on the left, right of height[i]

* Time-Complexity:
- Approach 1: in the worst case, push O(n) height[i] and pop O(n) height[i] so totally O(n)
- Approach 1: one pass from left to right to calculate left_max[i], one pass from right to left to calculate right_max[i],
and one pass to calculate what a slice contributes to the total water, so O(3n) = O(n)
* Space-Complexity:
- Approach 1: O(n) for the stack
- Approach 2: O(2n) for the left_max[], right_max[]
""""""

from collections import deque
def trappingWater_slice(height):
    n = len(height)
    if n == 1:
        return 0
    left_max = [0 for i in range(n)]
    right_max = [0 for i in range(n)]

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    water_total = 0
    for i in range(1, n-1):
        water_total += max(0, (min(left_max[i-1], right_max[i+1]) - height[i]))
    return water_total

def trappingWater_dp(height):
    n = len(height)
    if n == 0:
        return 0
    water = 0
    stack = deque()
    stack.append([0, height[0]])
    top = []
    for i in range(1, n):
        # print('stack = ', stack, f'consider height[{i}] = {height[i]}')
        while len(stack) >= 1 and height[i] >= stack[-1][1]:
            top = stack.pop()
            # print('pop top = ', top)
            water -= top[1]
            # print('water = ', water)
        if len(stack) == 0:
            water += (i - top[0])*top[1]
            # print(f'add {(i - top[0] - 1)*top[1]}')
        stack.append([i, height[i]])
    # print('final stack = ', stack)
    while len(stack) >= 2:
        top = stack.pop()
        water += (top[0] - stack[-1][0] - 1)*top[1]
        # print(f'add {(top[0] - stack[-1][0] - 1)*top[1]}')
    # print(f'--- final result: {water} vs {trappingWater_slice(height)}')
    return water

test = [[4,2,0,3,2,5], [1,1,0,2,1,0,1,3,2,1,2,1], [0,1,0,2,1,0,1,3,2,1,2,1]]
for e in test:
    print(trappingWater_dp(e))
