class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return False

        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        seen = set()
        q = deque()
        minutes = 0

        # add initial rotten fruits
        # go through every fruit
        # queue the ones that are rotten and haven't been seen
        # spread the rotten fruit and queue the next rotten fruit + add to seen
        # repeat

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        
        while q:
            r, c, mins = q.popleft() # our last mins should be our minutes taken
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, mins + 1))
            minutes = mins
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
                
        return minutes


