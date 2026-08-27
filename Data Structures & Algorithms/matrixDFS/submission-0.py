class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()

        # function recursively 
        def DFS(r, c):
            # base case
            # boundary
            if (r < 0 or r >= len(grid) 
            or c < 0 or c >= len(grid[0])
            or grid[r][c] == 1
            or (r, c) in visited):
                return 0

            # target cell
            if r == len(grid)-1 and c == len(grid[0])-1:
                return 1

            visited.add((r, c)) 

            paths = (
                DFS(r + 1, c)
                + DFS(r - 1, c)
                + DFS(r, c-1)
                + DFS(r, c+1)
            )

            visited.remove((r,c))

            return paths

        return DFS(0, 0)
