"""
* Problem: There are 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted
in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).
Write a program to move the disks from the first tower to the last so that
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
* Algorithm: move n disk from source to target using mid is done by moving n-1 disks from source to mid using target, and
then move the last disk from source to target, eventually move the n-1 disks from mid to target
* Time-Complexity: Let T(n) be the number of steps then T(n) = T(n-1) + 1 + T(n-1) = 2T(n-1) +1, by induction
T(n) = 2^n - 1
* Space-Complexity: The depth of the recusion is n-1 so the space complexity is O(2^n).
"""
def HanoiTower(n):
    @lru_cache
    def disk_move(source, target):
        print(source, '->', target)
    def hanoi_tower_solution(n, source, mid, target):
        if n == 1:
            disk_move(source, target)
        else:
            hanoi_tower_solution(n-1, source, target, mid)
            disk_move(source, target)
            hanoi_tower_solution(n-1, mid, source, target)
    hanoi_tower_solution(n, "S", "M", "T")

for n in range(1, 20):
    print("----- n = ", n)
    HanoiTower(n)