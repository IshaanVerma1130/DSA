def recur(adj: dict[list[int]], vis: list[int], curr: int) -> bool:
    if vis[curr] == True:
        return True

    vis[curr] = True
    flag = False

    for i in range(len(adj[curr])):
        flag = recur(adj, vis, adj[curr][i])
        if flag:
            return True

    return False


def detect(adj: dict[list[int]]) -> bool:
    vis = [False for _ in range(len(adj))]
    flag = False

    for i in range(len(adj)):
        vis[i] = True

        for j in range(len(adj[i])):
            flag = recur(adj, vis, adj[i][j])
            if flag:
                return True

        vis[i] = False

    return False


adj = {0: [1], 1: [], 2: [1, 3], 3: [4], 4: [0, 2]}
print(detect(adj))
