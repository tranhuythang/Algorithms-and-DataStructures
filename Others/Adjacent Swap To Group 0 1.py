"""
*Problem: Given a binary array, tell the minimum number of swapping two adjacent element so that all 0's are moved to one
end and all 1's are moved to the other end of the array.
*Algorithm: We calculate the number of moves to (i) move 0 to the left, (ii) move 1 to the left and take the min of them
From the final state where all 0 are moved to the left, we count number of moves to move 1 at the wrong position to the
smallest right position on the left.
*Time-complexity: O(n)
*Space-complexity: O(1)
"""
def AdjacentSwap(nums):
    finalized_1_count = 0
    finalized_0_count = 0
    move_1_count = 0
    move_0_count = 0

    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            move_1_count += (i - finalized_1_count)
            finalized_1_count += 1
        else:
            move_0_count += (i - finalized_0_count)
            finalized_0_count += 1
    return min(move_1_count, move_0_count)

input = [[0,1,0,1], [1,0,1,0,0,0,0,1], [1,0,0,0,0,1,0,1]]
for a in input:
    print(a, '->', AdjacentSwap(a))
