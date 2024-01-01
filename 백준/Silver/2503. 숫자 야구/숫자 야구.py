import sys
input = sys.stdin.readline

cnts = [[[0]*10 for _ in range(10)] for _ in range(10)]

N = int(input())
for _ in range(N):
    num, strike, ball = map(int, input().split())
    a, b, c = num//100, (num//10)%10, num%10
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                for k in range(1, 10):
                    if k != i and k != j:  # 숫자 조건 만족
                        tmps, tmpb = 0, 0
                        if i == a: tmps += 1
                        if j == b: tmps += 1
                        if k == c: tmps += 1
                        if i == b or i == c: tmpb += 1
                        if j == a or j == c: tmpb += 1
                        if k == a or k == b: tmpb += 1
                        if strike == tmps and ball == tmpb:
                            cnts[i][j][k] += 1

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if cnts[i][j][k] == N:
                res += 1
print(res)