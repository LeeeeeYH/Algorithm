# input = __import__('sys').stdin.readline
#
# b = list(map(int, input().split()))
# ls = [list(map(int, input().split())) for _ in range(5)]
#
# def recur(x, y):
#     if x < 0 or y < 0:
#         return True
#     if x == 0 and y == 0:
#         return False
#
#     ret = False
#     for i in b:
#         if not recur(x - i, y) or not recur(x, y - i):
#             ret = True
#             break
#
#     return ret
#
# for x, y in ls:
#     print('BA'[recur(x, y)])

import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

b = list(map(int, input().split()))
ls = [list(map(int, input().split())) for _ in range(5)]
dp = [[-1]*501 for _ in range(501)]

def recur(x, y):
    if x < 0 or y < 0:
        return True
    if x == 0 and y == 0:
        return False

    if dp[x][y] == -1:
        dp[x][y] = False
        for i in b:
            if not recur(x - i, y) or not recur(x, y - i):
                dp[x][y] = True
                break

    return dp[x][y]

for x, y in ls:
    print('BA'[recur(x, y)])