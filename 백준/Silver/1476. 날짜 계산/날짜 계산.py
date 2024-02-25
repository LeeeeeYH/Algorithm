input = __import__('sys').stdin.readline

E, S, M = map(int, input().split())
e, s, m, res = 1, 1, 1, 1
while True:
    if e==E and s==S and m==M:
        break

    e, s, m, res = e+1, s+1, m+1, res+1
    if e==16: e = 1
    if s==29: s = 1
    if m==20: m = 1

print(res)