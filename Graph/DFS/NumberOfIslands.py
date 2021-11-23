def NumberOfIslands_DFS(grid):
    n = len(grid)
    m = len(grid[0])

    connected_comp_count = 0
    visited = [[False for i in range(m)] for j in range(n)]

    def dfs(row, col):
        if grid[row][col] == '1' and not visited[row][col]:
            visited[row][col] = True
            if col < m-1:
                dfs(row, col+1)
            if col > 0:
                dfs(row, col-1)
            if row < n-1:
                dfs(row+1, col)
            if row > 0:
                dfs(row-1, col)

    for row in range(n):
        for col in range(m):
            if not visited[row][col] and grid[row][col] == '1':
                connected_comp_count += 1
                print(connected_comp_count, '-', row, col)
                dfs(row, col)
    return connected_comp_count

def NumberOfIslands_BFS(grid):


def main():
    test = [[["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]],
            [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]]
    for grid in test:
        print(NumberOfIslands_DFS(grid))

if __name__ == "__main__":
    main()

