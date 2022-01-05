"""
*Problem: 1642. Furthest Building You Can Reach
You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
While moving from building i to building i+1 (0-indexed),
- If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
- If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
*Algorithm:
Use ladders for the biggest height gaps; use bricks for the rest.
Use all bricks until we run out of bricks, at that time, replace the biggest height gap among the gap we use brick by ladder
and then update the leftover bricks and then repeat the process, i.e. keep using bricks until we cannot then replace bricks by ladders.
The fastest way to find the biggest height gap while keep inserting more height gap is to use Heap to store height gaps
*Time-Complexity:
Scan the height from left to right, at ith step, we have to push the height gap into the heap, which is having i elements,
so it takes O(log(i)), and hence totally, in the worst case,
O(log 1) + O(log 2) + ... + O(log N) = O(log N!) <= O(log N^N) = N log(N)
*Space-Complexity: N
"""
import heapq
def furthestBuilding(heights, bricks, ladders):
    n = len(heights)
    if n == 1:
        return 0
    gap_heap = []

    i = 0
    while i < n-1:
        gap = heights[i+1] - heights[i]
        if gap <= 0:
            i += 1
        else:
            heapq.heappush(gap_heap, -gap)
            if bricks >= gap:
                bricks -= gap
                i += 1
            else:
                while ladders >= 1 and bricks < gap:
                    ladders -= 1
                    bricks += (-heapq.heappop(gap_heap))
                if bricks < gap:
                    break
                else:
                    bricks -= gap
                    i += 1
    return i

test = [[[4,2,7,6,9,14,12], 5, 1]]
for t in test:
    print(furthestBuilding(t[0], t[1], t[2]))