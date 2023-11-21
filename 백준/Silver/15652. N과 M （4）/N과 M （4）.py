import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = [0] * M

def recur(cur, start):
    if cur == M:
        print(*num)
        return

    for i in range(start, N + 1):
        num[cur] = i
        recur(cur + 1, i)

recur(0, 1)