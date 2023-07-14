# 평범한 배낭
# 백트래킹, 탑다운

# N, K = map(int, input().split())
# WV = [list(map(int, input().split())) for _ in range(N)]
# dp = [[-1, 0] for _ in range(N + 4)]
#
# def recur(idx, sum):
#     if sum > K: return -100000000000000000
#     if idx == N: return 0
#
#     value = max(WV[idx][1] + recur(idx+1, sum+WV[idx][0]), recur(idx+1, sum))
#     return value
#
# print(recur(0, 0))

# 바텀업

N, K = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*101004 for _ in range(N)]


def recur(idx, sum):
    if sum > K: return -100000000000000000
    if idx == N: return 0

    if dp[idx][sum] == -1:
        dp[idx][sum] = max(WV[idx][1] + recur(idx+1, sum+WV[idx][0]), recur(idx+1, sum))
    return dp[idx][sum]

print(recur(0, 0))