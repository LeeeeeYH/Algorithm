import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

res = 0

# 기울기있는 선분 구하기
for dx in range(1, N+1):
    for dy in range(1, M+1):
        if gcd(dx, dy) == 1: # 서로소인 것만
            lx, ly = dx*(K-1), dy*(K-1) # 선분 x, y 길이
            if lx <= N and ly <= M:
                res += (N-lx+1)*(M-ly+1)

# 음수 기울기 계산
res *= 2
# x축, y축에 평행한 선분 개수
res += max(0, (N+1)*(M+2-K)) + max(0, (M+1)*(N+2-K))

print(res)