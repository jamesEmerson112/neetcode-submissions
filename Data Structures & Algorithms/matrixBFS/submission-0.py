from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # return helper for BFS
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        queue = deque()
        queue.append((0, 0))
        distance = 0
        visited = {(0, 0)}

        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                print(r, c)
                if r == rows -1 and c == cols-1:
                    return distance # this is the destination

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 0
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            distance += 1

        return -1


