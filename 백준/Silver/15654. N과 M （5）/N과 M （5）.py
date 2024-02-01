import sys
input = sys.stdin.readline

N, M = map(int, input().split())
origin = sorted(map(int, input().split()))
num = [0]*M

def recur(cur, flag):
    if cur == M:
        print(*num)
        return

    for i in range(N):
        if not flag & 1<<i:
            num[cur] = origin[i]
            recur(cur + 1, flag | 1<<i)

recur(0, 0)