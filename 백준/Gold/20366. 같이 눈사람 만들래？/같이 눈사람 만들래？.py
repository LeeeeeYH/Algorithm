import sys
input = sys.stdin.readline

N = int(input())
snows = sorted(map(int, input().split()))

def sol(num, ls):
    global res
    i, j = 0, len(ls)-1
    while i < j:
        diff = num - ls[j] - ls[i]
        res = min(res, abs(diff))
        if diff > 0:
            i += 1
        else:
            j -= 1

res = 1_000_000_000
for i in range(N-1):
    for j in range(i+1, N):
        sol(snows[i]+snows[j], snows[:i] + snows[i+1:j] + snows[j+1:])

print(res)