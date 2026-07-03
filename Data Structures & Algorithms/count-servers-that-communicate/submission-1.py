import copy

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        rowCount = [0] * ROWS
        colCount = [0] * COLS
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1

        count  = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (rowCount[r] > 1 or colCount[c] > 1):
                    count += 1
                    print(r,c)

        return count