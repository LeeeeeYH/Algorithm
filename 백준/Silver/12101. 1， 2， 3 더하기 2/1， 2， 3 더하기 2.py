import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0

def recur(nums, sum):
    if sum > n:
        return
    global cnt
    if sum == n:
        cnt += 1
        if cnt == k:
            print('+'.join(nums))
            exit(0)

    for i in range(1, 4):
        recur(nums+[str(i)], sum+i)

recur([], 0)
print(-1)