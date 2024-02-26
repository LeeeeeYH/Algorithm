# input = __import__('sys').stdin.readline
#
# def recur(cur):  # 내가 질 수 있는가
#     if cur < 0:  # 잘못된 입력
#         return True
#     if cur == 0:  # 내가 짐
#         return False
#
#     # 하나라도 상대방이 지는 상황이 있다면 True여야함
#     # ==> recur(cur-i)가 하나라도 False면 True를 반환해야함
#     return not(recur(cur-1) and recur(cur-3) and recur(cur-4))
#
# print('SK' if recur(int(input())) else 'CY')

import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

N = int(input())
dp = [-1] * (N+1)

def recur(cur):  # 내가 질 수 있는가
    if cur < 0:  # 잘못된 입력
        return True
    if cur == 0:  # 내가 짐
        return False

    # 하나라도 상대방이 지는 상황이 있다면 True여야함
    # ==> recur(cur-i)가 하나라도 False면 True를 반환해야함
    if dp[cur] == -1:
        dp[cur] = not(recur(cur-1) and recur(cur-3) and recur(cur-4))
    return dp[cur]

print('SK' if recur(N) else 'CY')
