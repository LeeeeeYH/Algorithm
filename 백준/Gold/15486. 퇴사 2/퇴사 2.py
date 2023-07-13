#퇴사2
#탑다운

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 9)
#
# N = int(input())
# TP = [list(map(int, input().split())) for _ in range(N)]
# dp = [-1] * 1500004
#
# def recur(idx): # 날짜, 이득
#     if idx > N:
#         return -1000000000000
#     if idx == N:
#         return 0
#
#     if dp[idx] == -1:
#         dp[idx] = max(TP[idx][1] + recur(idx+TP[idx][0]), recur(idx+1))
#     return dp[idx]
#
# recur(0)
# print(dp[0])

#퇴사2
#바텀업

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]
dp = [-1000000000000] * 1_500_054 # if idx > N: return -1000000000000
dp[N] = 0 # if idx == N: return 0

for i in range(N)[::-1]:
    dp[i] = max(TP[i][1] + dp[i+TP[i][0]], dp[i+1])
#   dp[idx] = max(TP[idx][1] + recur(idx+TP[idx][0]), recur(idx+1)) 탑다운의 수식과 유사

print(dp[0])