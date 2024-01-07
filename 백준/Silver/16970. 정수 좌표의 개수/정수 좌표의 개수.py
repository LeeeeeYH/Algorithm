import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
res = 0

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# 가로세로 아닌 선분의 (서로소인)기울기로 구하기
for x in range(1, N+1):
    for y in range(1, M+1):
        if gcd(x, y) == 1:  # 기울기 x, y가 서로소 -> 선분의 점이 2개
            xk, yk = x*(K-1), y*(K-1)  # 점이 K개인 선분
            if xk <= N and yk <= M:
                res += (N - xk + 1)*(M - yk + 1)

# 음수 기울기
res *= 2

# 가로선분, 세로선분
res += max(0, (M+1)*(N-K+2)) + max(0, (N+1)*(M-K+2))

print(res)