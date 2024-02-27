input = __import__('sys').stdin.readline

a = " " + input().rstrip()
b = " " + input().rstrip()
lena = len(a)-1
lenb = len(b)-1
dp = [[0]*(lenb+1) for _ in range(lena+1)]

for i in range(1, lena+1):
    for j in range(1, lenb+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[lena][lenb])