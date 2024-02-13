import sys
input = sys.stdin.readline

N = int(input())
ls = []
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    ls.append([x, y])
    X.append(x)
    Y.append(y)
res = [100_000_000] * N

def check(x, y):
    # (x, y)와 가까운 순서대로 저장
    diss = sorted([abs(a-x) + abs(b-y) for a, b in ls])

    summ = 0
    for i in range(N):
        summ += diss[i]
        res[i] = min(res[i], summ)  # (x, y)에 대해 체커가 i개 일때 최소거리


for x in X:
    for y in Y:
        check(x, y)
print(*res)
