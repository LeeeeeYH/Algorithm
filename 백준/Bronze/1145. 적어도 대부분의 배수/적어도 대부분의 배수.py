import sys
input = sys.stdin.readline

ls = list(map(int, input().split()))

res = 0
while True:
    cnt = 0
    res += 1

    for i in ls:
        if res % i == 0:
            cnt += 1

    if cnt >= 3:
        break

print(res)
