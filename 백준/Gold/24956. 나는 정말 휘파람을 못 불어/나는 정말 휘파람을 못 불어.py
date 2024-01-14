import sys
input = sys.stdin.readline

N = int(input()) + 1
S = " " + input().rstrip()
W, H, E = [0]*(N+1), [], [0]*(N+1)

for i in range(1, N):
    b = N-i  # 뒤에서부터 index
    W[i], E[b] = W[i-1], E[b+1]
    if S[i] == 'W':  # 앞에서부터 W가 몇개있냐
        W[i] += 1
    if S[i] == 'H':  # H의 index들
        H.append(i)
    if S[b] == 'E':  # 뒤에서부터 E가 몇개있냐
        E[b] += 1

res = 0
# H기준으로 왼쪽에 W개수 X 오른쪽에 E중 2개를 뽑는 경우의수(부분집합 - 한개만 - 0개뽑을때)
for h in H:
    res += W[h]*(2**E[h] - E[h] - 1)
print(res%1_000_000_007)