import sys
input = sys.stdin.readline

N = int(input())
Ai = list(map(int, input().split()))
a, s, m, d = map(int, input().split())
maxi, mini = -1_000_000_000, 1_000_000_000

def div(a, b):
    if a < 0 < b:
        return -((-a)//b)
    else:
        return a//b

def recur(cur, num, a, s, m, d):
    if cur == N:
        global maxi, mini
        maxi = max(maxi, num)
        mini = min(mini, num)
        return

    if a:
        recur(cur+1, num+Ai[cur], a-1, s, m, d)
    if s:
        recur(cur+1, num-Ai[cur], a, s-1, m, d)
    if m:
        recur(cur+1, num*Ai[cur], a, s, m-1, d)
    if d:
        recur(cur+1, div(num, Ai[cur]), a, s, m, d-1)

recur(1, Ai[0], a, s, m, d)
print(maxi)
print(mini)