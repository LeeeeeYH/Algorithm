import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if N == K:
    print(0)
    print(N)
    exit(0)

q = []
ls = [-1] * 100001
res = []

q.append(N)
ls[N] = N

while True:
    cur = q.pop(0)
    if cur == K:
        res.append(cur)
        p = ls[cur]
        while p != ls[p]:
            res.append(p)
            p = ls[p]
        res.append(p)
        print(len(res)-1)
        print(*res[::-1])
        break

    for next in [cur-1, cur+1, cur*2]:
        if 0 <= next <= 100000 and ls[next] == -1:
            q.append(next)
            ls[next] = cur