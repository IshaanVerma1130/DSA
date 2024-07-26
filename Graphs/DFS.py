class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs(self, start):
        visited = set()

        def dfs_recursive(node):
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    dfs_recursive(neighbor)

        dfs_recursive(start)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Traversal (starting from vertex 2):")
g.dfs(2)
