import sys
input = sys.stdin.readline

N = int(input())
cols = [0]*N

def check(n):
    for i in range(n):
        if cols[i] == cols[n] or abs(i-n) == abs(cols[i] - cols[n]):
            return False
    return True

res = 0
def recur(cur):
    if cur == N:
        global res
        res += 1
        return

    for i in range(N):
        cols[cur] = i
        if check(cur):
            recur(cur+1)

recur(0)
print(res)