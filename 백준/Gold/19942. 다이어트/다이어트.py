import sys
input = sys.stdin.readline

N = int(input())
min_nut = list(map(int, input().split()))
ings = [list(map(int, input().split())) for _ in range(N)]
res = []
min_price = 7501

def recur(cur, sum, check):
    if cur == N:
        for i in range(4):
            if sum[i] < min_nut[i]:
                break
        else:
            global res, min_price
            if min_price > sum[4]:
                min_price = sum[4]
                res = [[i+1 for i in range(N) if check & 1<<i]]
            elif min_price == sum[4]:
                res += [[i+1 for i in range(N) if check & 1<<i]]
        return

    recur(cur+1, [sum[i]+ings[cur][i] for i in range(5)], check | 1<<cur)
    recur(cur+1, sum, check)

recur(0, [0]*5, 0)
if min_price == 7501:
    print(-1)
else:
    print(min_price)
    print(*(sorted(res)[0]))