import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
res = 0

def recur(cur, summ, check):
    if cur == N:
        if check and summ == S:
            global res
            res += 1
        return

    recur(cur+1, summ + nums[cur], check|True)
    recur(cur+1, summ, check)

recur(0, 0, False)
print(res)