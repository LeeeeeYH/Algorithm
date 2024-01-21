import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ls = list(map(int, input().split()))
even = [False if i%2 else True for i in ls]

i, dele, leng = 0, 0, 0
res = 0
for j in range(N):
    leng += 1
    if not even[j]:
        dele += 1
    if dele <= K:
        res = max(res, leng-dele)

    while dele > K:
        if not even[i]:
            dele -= 1
        i, leng = i+1, leng-1

print(res)