import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    d, n = map(int, input().split())
    ls = list(map(int, input().split()))

    summ, res = 0, 0
    mod = dict()
    mod[0] = 1
    for i in ls:
        summ = (summ+i) % d
        if summ in mod:
            res += mod[summ]
            mod[summ] += 1
        else:
            mod[summ] = 1

    print(res)