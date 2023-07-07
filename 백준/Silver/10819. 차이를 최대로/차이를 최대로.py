import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
res = 0

def recur(cur, last, total, check):
    global res
    if cur == N:
        if res < total:
            res = total

    for i in range(N):
        if not check & 1<<i:
            recur(cur+1, nums[i], total+abs(last - nums[i]), check | 1<<i)

for i in range(N):
    recur(1, nums[i], 0, 1<<i)
print(res)