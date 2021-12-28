"""
* Problem: 1046. Last Stone Weight
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
•	If x == y, both stones are destroyed, and
•	If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the smallest possible weight of the left stone. If there are no stones left, return 0.
* Algorithm: use max-heap data structure to store the stone weight since we keep needing the max element
Keep smashing two stones, if resulting in a stone, push it to the max-heap data structure.
* Time-complexity: O(nlogn) due to heap
* Space-complexity: Auxiliary space is just O(1) because heapify (converting list to a heap) is done In-Place.
"""
import heapq
def lastStoneWeight(stones):
    neg_stones = [-stones[i] for i in range(len(stones))]
    heapq.heapify(neg_stones)
    while len(neg_stones) >= 2:
        max1 = - heapq.heappop(neg_stones)
        max2 = - heapq.heappop(neg_stones)
        residue = max1 - max2
        if residue > 0:
            heapq.heappush(neg_stones, -residue)
    if len(neg_stones) == 1:
        return - neg_stones[0]
    else:
        return 0

