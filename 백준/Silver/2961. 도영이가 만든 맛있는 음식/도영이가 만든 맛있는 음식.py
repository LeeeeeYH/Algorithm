import sys
input = sys.stdin.readline

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
res = 1_000_000_000

def recur(cur, s, b, used):
    if cur == N:
        if used:
            global res
            res = min(res, abs(s - b))
        return

    recur(cur+1, s*ls[cur][0], b+ls[cur][1], True)
    recur(cur+1, s, b, used)

recur(0, 1, 0, False)
print(res)