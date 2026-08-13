class Graph:
    
    def __init__(self):
        # so vertices
        # and edges
        self.hash_table = {}

    def addEdge(self, src: int, dst: int) -> None:

        if src not in self.hash_table:
            self.hash_table[src] = set()

        if dst not in self.hash_table:
            self.hash_table[dst] = set()

        self.hash_table[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.hash_table:
            return False

        if dst not in self.hash_table[src]:
            return False

        self.hash_table[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()

        def dfs(node):
            if node == dst:
                return True

            if node in visited:
                return False

            visited.add(node)

            for neighbor in self.hash_table[node]:
                if dfs(neighbor):
                    return True

            return False

        return dfs(src)
