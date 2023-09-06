import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
made = [False] * 100001 * 20

def recur(cur, total):
    if cur == N:
        made[total] = True
        return

    recur(cur+1, total)
    recur(cur+1, total+S[cur])

recur(0, 0)
for i in range(1, 100001*20):
    if not made[i]:
        print(i)
        exit(0)