import sys
input = sys.stdin.readline

N = int(input()) + 1
S = " " + input().rstrip()
W, H, E = [0]*(N+1), [], [0]*(N+1)

for i in range(1, N):
    b = N-i  # 뒤에서부터 index
    W[i], E[b] = W[i-1], E[b+1]
    if S[i] == 'W':
        W[i] += 1
    if S[i] == 'H':
        H.append(i)
    if S[b] == 'E':
        E[b] += 1

res = 0
for h in H:
    res += W[h]*(2**E[h] - E[h] - 1)
print(res%1_000_000_007)