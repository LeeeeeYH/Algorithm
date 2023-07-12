import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
alive = [True] * 10
if M != 0:
    for i in list(map(int, input().split())):
        alive[i] = False
buttons = [i for i in range(10) if alive[i]]

res = abs(N-100)
def recur(cur, count):
    global res
    res = min(res, abs(cur - N) + count)

    for i in buttons:
        next = cur*10 + i
        if abs(next - N) < abs(cur - N):
            recur(next, count+1)

for i in buttons:
    recur(i, 1)
print(res)