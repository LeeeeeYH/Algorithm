input = __import__('sys').stdin.readline

for _ in range(3):
    ls = list(map(int, input().split()))
    t = ls[3]*3600 + ls[4]*60 + ls[5] - (ls[0]*3600 + ls[1]*60 + ls[2])
    print(t//3600, t%3600//60, t%60)