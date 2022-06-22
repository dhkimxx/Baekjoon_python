from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
    exit()
INF = 500000
visited = [[0] * 2 for _ in range(INF + 1)]
flag = False
turn = 1
q = deque([N])
visited[N][0] = 1
while q:
    K += turn
    if K > INF:
        break
    if visited[K][turn % 2]:
        flag = True
        break
    for j in range(len(q)):
        v = q.popleft()
        for nv in [v + 1, v - 1, v * 2]:
            if 0 <= nv <= INF and not visited[nv][turn % 2]:
                visited[nv][turn % 2] = 1
                q.append(nv)
                if nv == K:
                    flag = True
                    break
        if flag:
            break
    if flag:
        break
    turn += 1
if flag:
    print(turn)
else:
    print(-1)
