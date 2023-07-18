# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# def recur(cur):
#     if cur < 0: # 상대방 잘못
#         return True
#     if cur == 0: # 상대방이 막타
#         return False
#
#     canwin = False
#     for i in [1, 3, 4]:
#         if not recur(cur - i):
#             canwin = True
#             break
#
#     return canwin
#
# print('SK' if recur(N) else 'CY')

# 백트를 dp로

import sys
input = sys.stdin.readline

N = int(input())
check = [False] * 1004
dp = [False] * 1004

def recur(cur):
    if cur < 0: # 상대방 잘못
        return True
    if cur == 0: # 상대방이 막타
        return False

    if not check[cur]: # 계산 안해봤으면
        check[cur] = True
        for i in [1, 3, 4]:
            if not recur(cur - i):
                dp[cur] = True
                break

    return dp[cur]

print('SK' if recur(N) else 'CY')