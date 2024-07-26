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


def Solve(prerequisites: list[list[int]]) -> bool:
    adj = {}
    for el in prerequisites:
        if el[0] in adj:
            el[0].append(el[1])
        else:
            el[0] = [el[1]]
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


prerequisites = [[1, 0], [0, 1]]
print(Solve(prerequisites))
