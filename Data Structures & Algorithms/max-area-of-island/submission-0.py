class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        # grid but it's for isVisited
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        # recursion function to recursively go up, down, left, right to find if grid[x][y] is 1
        def dfs(x, y):
            # base case
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 0
            if grid[x][y] == 0 or visited[x][y]:
                return 0

            visited[x][y] = True

            area = 1  # current cell

            # explore neighbors
            area += dfs(x + 1, y)
            area += dfs(x - 1, y)
            area += dfs(x, y + 1)
            area += dfs(x, y - 1)

            return area
        
        # iterate through the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)  

        return max_area