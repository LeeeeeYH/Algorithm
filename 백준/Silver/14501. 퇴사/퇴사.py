import sys
input = sys.stdin.readline

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]

def recur(cur):
    if cur > N:
        return -98765321
    if cur == N:
        return 0

    return max(recur(cur+ls[cur][0]) + ls[cur][1], recur(cur+1))

print(recur(0))