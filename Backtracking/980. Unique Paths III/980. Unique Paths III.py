from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total += 1
                if grid[i][j] == 1:
                    sx, sy = i, j

        def dfs(x, y, left):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
                return 0

            if grid[x][y] == 2:
                return 1 if left == 1 else 0

            temp = grid[x][y]
            grid[x][y] = -1

            ans = (
                dfs(x + 1, y, left - 1) +
                dfs(x - 1, y, left - 1) +
                dfs(x, y + 1, left - 1) +
                dfs(x, y - 1, left - 1)
            )

            grid[x][y] = temp
            return ans

        return dfs(sx, sy, total)