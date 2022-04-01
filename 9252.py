A, B = input(), input()
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            print(i, j, A[i - 1], B[j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

LCS = []
i = len(A)
j = len(B)

while i > 0 and j > 0:
    if dp[i][j - 1] == dp[i][j] - 1 and dp[i - 1][j] == dp[i][j] - 1:
        LCS.append(A[i - 1])
        i -= 1
        j -= 1
    else:
        if dp[i][j - 1] > dp[i - 1][j]:
            j -= 1
        else:
            i -= 1

print(dp[-1][-1])
print(''.join(map(str, reversed(LCS))))
