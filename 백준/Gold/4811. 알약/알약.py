import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

def recur(W, H):
    if W < 0 or H < 0:
        return 0
    if W == 0 and H == 0:
        return 1

    if dp[W][H] == -1:
        dp[W][H] = recur(W-1, H+1) + recur(W, H-1)
    return dp[W][H]

while True:
    N = int(input())
    dp = [[-1]*61 for _ in range(31)]
    if N == 0:
        break

    print(recur(N, 0))