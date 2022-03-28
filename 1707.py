import sys

def dfs(v, c):
    visited[v] = c
    if c == 1:
        nc = 2
    if c == 2:
        nc = 1

    for nv in graph[v]:
        if visited[nv] == '0':
            dfs(nv, nc)
        elif visited[nv] != nc:
            result = 'NO'

K = int(sys.stdin.readline())
for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for e in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    check = 1
    result = 'YES'
    for i in range(1, V + 1):
        if visited[i] == '0':
            dfs(i, check)
    print(result)
