import sys
input = sys.stdin.readline

N = int(input())
c = [0] + list(map(int, input().split()))
dcs = [[]]
for _ in range(N):
    p = int(input())
    dcs.append([list(map(int, input().split())) for _ in range(p)])

res = 10000
def recur(cur, price, summ, flag):
    if cur == N+1:
        global res
        res = min(res, summ)
        return

    for i in range(1, N+1):
        if not flag & 1<<i:
            nprice = price[:]
            for a, d in dcs[i]:
                nprice[a] = max(1, nprice[a] - d)
            recur(cur+1, nprice, summ + price[i], flag | 1<<i)

recur(1, c, 0, 0)
print(res)