# input = __import__('sys').stdin.readline
#
# N = int(input())
#
# def recur(cur):
#     if cur < 10:
#         return False
#
#     scur = str(cur)
#     leng = len(scur)
#     # 하나라도 상대가 지는 경우가 있으면 True
#     for i in range(1, leng):
#         for j in range(leng+1-i):
#             sub = int(scur[j:j+i])
#             if sub > 0 and not recur(cur - sub):
#                 return True
#     return False
#
# print(recur(N))

# import sys
# sys.setrecursionlimit(1_000_000)
# input = sys.stdin.readline
#
# N = int(input())
# dp = [-1]*1_000_001
# minn = 1_000_000
#
# def recur(cur, first):
#     if cur < 10:
#         return False
#
#     if dp[cur] == -1:
#         dp[cur] = False
#         scur = str(cur)
#         leng = len(scur)
#         # 하나라도 상대가 지는 경우가 있으면 True
#         for i in range(1, leng):
#             for j in range(leng+1-i):
#                 sub = int(scur[j:j+i])
#                 if sub > 0 and not recur(cur - sub, False):
#                     dp[cur] = True
#                     if first:
#                         global minn
#                         minn = min(minn, sub)
#     return dp[cur]
#
# if recur(N, True):
#     print(minn)
# else:
#     print(-1)

input = __import__('sys').stdin.readline

N = int(input())
dp = [-1]*1_000_001
dp[:10] = [False]*10
for cur in range(10, N + 1):
    scur = str(cur)
    leng = len(scur)
    dp[cur] = False
    for i in range(1, leng):
        for j in range(leng+1-i):
            sub = int(scur[j:j+i])
            if sub > 0 and not dp[cur - sub]:
                dp[cur] = True
                break
        if dp[cur]:
            break

# 바텀업에선 그냥 한번 더 구해봤다
minn = 1_000_000
if dp[N]:
    scur = str(N)
    leng = len(scur)
    for i in range(1, leng):
        for j in range(leng+1-i):
            sub = int(scur[j:j+i])
            if sub > 0 and not dp[N-sub]:
                minn = min(minn, sub)
    print(minn)
else:
    print(-1)