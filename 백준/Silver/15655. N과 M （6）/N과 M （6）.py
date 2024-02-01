import sys
input = sys.stdin.readline

N, M = map(int, input().split())
origin = sorted(map(int, input().split()))
num = [0]*M

def recur(cur, start):
    if cur == M:
        print(*num)
        return

    for i in range(start, N):
        num[cur] = origin[i]
        recur(cur + 1, i+1)

recur(0, 0)