input = __import__('sys').stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    res = set()
    for b in range(2, n):
        for a in range(1, b):
            if (a*a+b*b+m)//(a*b) == (a*a+b*b+m)/(a*b):
                res.add((a, b))
    print(len(res))