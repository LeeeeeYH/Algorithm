import sys
input = sys.stdin.readline

N, M = map(int, input().split())
inp = sorted(map(int, input().split()))
num = [0] * M

def recur(cur):
    if cur == M:
        print(*num)
        return

    for i in range(N):
        num[cur] = inp[i]
        recur(cur + 1)

recur(0)