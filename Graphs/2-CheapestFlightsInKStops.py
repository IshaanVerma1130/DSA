fare = 1000000000000000


def recur(
    adj: list[list[int]],
    cost: list[list[int]],
    src: int,
    dst: int,
    k: int,
    totalCost: int,
    visited: list[bool],
):
    global fare
    if k < -1:
        return
    if src == dst:
        fare = min(fare, totalCost)
        return

    visited[src] = True

    for i in range(len(adj[src])):
        if not visited[adj[src][i]] and (totalCost + cost[src][adj[src][i]] <= fare):
            recur(
                adj,
                cost,
                adj[src][i],
                dst,
                k - 1,
                totalCost + cost[src][adj[src][i]],
                visited,
            )

    visited[src] = False


def Solve(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    global fare
    adj = [[] for _ in range(n)]
    cost = [[0 for i in range(n)] for j in range(n)]

    for i in range(len(flights)):
        adj[flights[i][0]].append(flights[i][1])
        cost[flights[i][0]][flights[i][1]] = flights[i][2]

    visited = [False for _ in range(n)]
    recur(adj, cost, src, dst, k, 0, visited)
    if fare == 1000000000000000:
        return -1
    return fare


n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 0
print(Solve(n, flights, src, dst, k))
