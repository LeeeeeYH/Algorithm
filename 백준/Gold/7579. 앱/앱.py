# input = __import__('sys').stdin.readline
#
# N, M = map(int, input().split())
# m = list(map(int, input().split()))
# c = list(map(int, input().split()))
#
# # Memory 기준으로 하면 10억개의 배열이 필요하므로 메모리초과.
# # 비활성화 비용 C를 기준으로 새로운 관점으로 처리
# def recur(cur, usable):
#     if cur == N:
#         return 0
#
#     ret = recur(cur+1, usable)
#     if usable >= c[cur]:
#         ret = max(ret, recur(cur+1, usable-c[cur]) + m[cur])
#     return ret
#
# for i in range(10001):
#     print(recur(0, i))
#     if recur(0, i) >= M:
#         print(i)
#         exit(0)

import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [[-1]*10001 for _ in range(100)]

# Memory 기준으로 하면 10억개의 배열이 필요하므로 메모리초과.
# 비활성화 비용 C를 기준으로 새로운 관점으로 처리
def recur(cur, usable):
    if cur == N:
        return 0

    if dp[cur][usable] == -1:
        dp[cur][usable] = recur(cur+1, usable)
        if usable >= c[cur]:
            dp[cur][usable] = max(dp[cur][usable], recur(cur+1, usable-c[cur]) + m[cur])
    return dp[cur][usable]

for i in range(10001):
    if recur(0, i) >= M:
        print(i)
        exit(0)