input = __import__('sys').stdin.readline

N, K = map(int, input().split())
ls = list(map(int, input().split(',')))

for i in range(K):
    for j in range(N-1 - i):
        ls[j] = ls[j+1] - ls[j]

print(*ls[:N-K], sep=",")