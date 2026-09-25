class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        numIslands = 0

        def dfs(r, c):
            seen.add((r, c)) # add to visited
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    numIslands += 1
                    dfs(r,c)
        
        
        return numIslands

        