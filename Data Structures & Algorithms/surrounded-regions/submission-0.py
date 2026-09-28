class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # check for everything outside, and mark them as notSurrounded, turn everything else into X

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        rows = len(board)
        cols = len(board[0])

        safe = set()

        def dfs(r, c):
            safe.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in safe and board[nr][nc] == "O":
                    dfs(nr, nc)

        # first pass, check all the columns and rows
        for r in range(rows):
            if (r, 0) not in safe and board[r][0] == "O":
                dfs(r, 0)

            if (r, cols - 1) not in safe and board[r][cols -1] == "O":
                dfs(r, cols - 1)
        
        for c in range(cols):
            if (0, c) not in safe and board[0][c] == "O":
                dfs(0, c)
            
            if (rows - 1, c) not in safe and board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
