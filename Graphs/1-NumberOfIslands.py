def mark(graph, i, j, n, m):
    if i < 0 or j < 0 or i >= n or j >= m or graph[i][j] != 1:
        return

    graph[i][j] = 2

    mark(graph, i + 1, j, n, m)
    mark(graph, i - 1, j, n, m)
    mark(graph, i, j + 1, n, m)
    mark(graph, i, j - 1, n, m)


def Solve(graph: list[list[int]]) -> int:
    n = len(graph)

    if n == 0:
        return 0

    m = len(graph[0])

    islands = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                mark(graph, i, j, n, m)
                islands += 1

    return islands


graph = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
print(Solve(graph))
