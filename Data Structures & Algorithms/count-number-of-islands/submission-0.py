class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        isVisited = [[False] * COLS for y in range(ROWS)]

        def recursive(x,y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                return
            if isVisited[x][y] == True:
                return
            if grid[x][y] == '0':
                return

            isVisited[x][y] = True
            
            recursive(x, y-1) 
            recursive(x, y+1)
            recursive(x-1, y)
            recursive(x+1,y)

        count = 0
        for x in range(ROWS):
            for y in range(COLS):
                if isVisited[x][y] == False and grid[x][y] == '1': # it's for unexplored land
                    count += 1
                    # print(x,y)
                    recursive(x,y)

        return count
