import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
dots = set()
for _ in range(N):
    dots.add(tuple(map(int, input().split())))

res = 0
for i in dots:
    if (i[0] + A, i[1]) in dots and (i[0], i[1] + B) in dots and (i[0] + A, i[1] + B) in dots:
        res += 1
print(res)