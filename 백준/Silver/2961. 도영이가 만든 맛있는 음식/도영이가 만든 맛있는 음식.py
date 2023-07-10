import sys
input = sys.stdin.readline

N = int(input())
ings = [list(map(int, input().split())) for _ in range(N)]
res = 10**9

def recur(cur, S_mul, B_sum, cnt):
    if cur == N:
        if cnt != 0:
            global res
            res = min(res, abs(S_mul - B_sum))
        return

    recur(cur+1, S_mul*ings[cur][0], B_sum + ings[cur][1], cnt+1)
    recur(cur+1, S_mul, B_sum, cnt)

recur(0, 1, 0, 0)
print(res)