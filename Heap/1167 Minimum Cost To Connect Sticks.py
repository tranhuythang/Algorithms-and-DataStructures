"""
* Problem: 1167. Minimum Cost to Connect Sticks
You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.
You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.
Return the minimum cost of connecting all the given sticks into one stick in this way.
Input: sticks = [2,4,3]
Output: 14
Explanation: You start with sticks = [2,4,3].
1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
* Algorithm:
Always connect the two shortest sticks. Note that after connecting two shortest sticks into one stick, we put the newly
joined stick back to the list and then choose the shortest stick from there.
Since we need to take out the min and then insert new element to the list, the best data structure is heap.
* Time-complexity:
Step 1: O(log1) + O(log2) + ... + O(logn) = O(nlogn) to make a heap from the list of sticks
Step 2: the loop
[O(logn) + O(log(n-1))] + [O(log(n-1)) + O(log(n-2))] + ... + [log2 + log1] = 2 O(nlogn)
so still O(nlogn)
* Space-complexity: O(n)
"""
import heapq
def connectSticks(sticks):
    n = len(sticks)
    if n == 1:
        return 0

    stick_heap = sticks[::]
    heapq.heapify(stick_heap)
    result = 0
    stick1 = stick2 = joined_stick = 0
    while len(stick_heap) > 1:
        stick1 = heapq.heappop(stick_heap)
        stick2 = heapq.heappop(stick_heap)
        joined_stick = stick1 + stick2
        result += joined_stick
        heapq.heappush(stick_heap, joined_stick)
    return result
