def HanoiTower(n):
    def disk_move(source, target):
        print(source, '->', target)
    def hanoi_tower_solution(n, source, mid, target):
        if n == 1:
            disk_move(source, target)
        else:
            hanoi_tower_solution(n-1, source, target, mid)
            disk_move(source, target)
            hanoi_tower_solution(n - 1, mid, source, target)
    hanoi_tower_solution(n, "S", "M", "T")

for n in range(1, 7):
    print("----- n = ", n)
    HanoiTower(n)