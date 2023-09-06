# import sys
# input = sys.stdin.readline
#
# ls = list(map(int, input().split()))
#
# def recur(a, b):
#     if a < 0 or b < 0: # 잘못하는 방법이 하나라도 있으면?
#         return True
#     if a == 0 and b == 0: # 이기면?
#         return False
#
#     ret = False
#     for i in ls: # 한번이라도 False가 있다면(이기는 방법이 있다면)
#         ret |= not recur(a - i, b)
#         ret |= not recur(a, b - i)
#
#     return ret
#
# for _ in range(5):
#     k1, k2 = map(int, input().split())
#     print('A' if recur(k1, k2) else 'B')


# 백트를 dp로

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

ls = list(map(int, input().split()))
dp = [[False]*501 for _ in range(501)]
check = [[False]*501 for _ in range(501)]


def recur(a, b):
    if a < 0 or b < 0: # 잘못하는 방법이 하나라도 있으면?
        return True
    if a == 0 and b == 0: # 이기면?
        return False

    if not check[a][b]:
        check[a][b] = True
        for i in ls: # 한번이라도 False가 있다면(이기는 방법이 있다면)
            dp[a][b] |= not recur(a - i, b)
            dp[a][b] |= not recur(a, b - i)

    return dp[a][b]

for _ in range(5):
    k1, k2 = map(int, input().split())
    print('A' if recur(k1, k2) else 'B')