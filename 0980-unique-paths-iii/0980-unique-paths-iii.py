class Solution:
    def uniquePathsIII(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        empty = 0
        start_r = start_c = 0

        # Find starting point and count cells we must visit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != -1:
                    empty += 1

                if grid[r][c] == 1:
                    start_r = r
                    start_c = c

        def dfs(r, c, count):
            # Out of bounds or obstacle
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == -1:
                return 0

            # Reached ending point
            if grid[r][c] == 2:
                return 1 if count == empty else 0

            # Mark current cell as visited
            grid[r][c] = -1

            paths = (
                dfs(r + 1, c, count + 1) +
                dfs(r - 1, c, count + 1) +
                dfs(r, c + 1, count + 1) +
                dfs(r, c - 1, count + 1)
            )

            # Backtrack
            grid[r][c] = 0

            return paths

        return dfs(start_r, start_c, 1)