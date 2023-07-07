import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

res = 0
def recur(cur, num):
    global res
    if cur == N:
        if num == S:
            res += 1
        return

    recur(cur + 1, num + nums[cur])
    recur(cur + 1, num)

recur(0, 0)
print(res - int(S==0))