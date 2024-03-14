input = __import__('sys').stdin.readline

N = int(input())
ls = list(map(int, input().split()))
Y, M = 0, 0
for i in ls:
    Y += (i//30 + 1) * 10
    M += (i//60 + 1) * 15

if Y < M:
    print('Y', Y)
elif Y > M:
    print('M', M)
else:
    print('Y M', Y)