import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.reverse()
dp = [1] * N
for i in range(0, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
'''
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1] * N
for i in range(0, N):
    for j in range(0, i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
'''