input = __import__('sys').stdin.readline

N = int(input())
Bi = [int(input()) for _ in range(N)]
have = set(Bi)
Bi += [-1]
res = 0
for ban in have:
    bf = -1
    cnt = 0
    for i in Bi:
        if i == ban:
            continue

        if i == bf:
            cnt += 1
        else:
            res = max(res, cnt)
            bf = i
            cnt = 1
print(res)