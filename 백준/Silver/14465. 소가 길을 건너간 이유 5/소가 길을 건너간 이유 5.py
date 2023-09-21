import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
ls = [0] * (N+1)  # 0: 멀쩡한 신호등, 1: 고장난 신호등
for i in range(B):
    ls[int(input())] = 1

s = sum(ls[1:K+1])  # 1~K까지 고장난 신호등의 개수로 초기화
res = s

for i in range(K+1, N+1):
    s += ls[i] - ls[i-K]
    res = min(res, s)
print(res)
