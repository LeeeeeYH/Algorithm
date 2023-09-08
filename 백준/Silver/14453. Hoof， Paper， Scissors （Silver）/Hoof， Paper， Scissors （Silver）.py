import sys
input = sys.stdin.readline

N = int(input())
H, P, S = [0]*(N+1), [0]*(N+1), [0]*(N+1)

for i in range(1, N+1):
    inp = input().rstrip()
    if inp == 'H':
        H[i] = H[i - 1]+1
        P[i] = P[i - 1]
        S[i] = S[i - 1]
    elif inp == 'P':
        H[i] = H[i - 1]
        P[i] = P[i - 1]+1
        S[i] = S[i - 1]
    elif inp == 'S':
        H[i] = H[i - 1]
        P[i] = P[i - 1]
        S[i] = S[i - 1]+1

res = 0
for i in range(1, N+1):
    res = max(res,
              H[i] + P[N]-P[i], H[i] + S[N]-S[i],
              P[i] + H[N]-H[i], P[i] + S[N]-S[i],
              S[i] + H[N]-H[i], S[i] + P[N]-P[i])

print(res)