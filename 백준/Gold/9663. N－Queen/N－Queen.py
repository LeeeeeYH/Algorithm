import sys
input = sys.stdin.readline

N = int(input())
cols = [0] * N
res = 0

def check(idx): # 행 번호, 몇 번째 열에 놓을지
    for i in range(idx): # 이전까지의 행에 대해서
        if cols[idx] == cols[i] or abs(idx - i) == abs(cols[idx] - cols[i]):
            return False
    return True

def recur(cur):
    global res
    if cur == N:
        res += 1
        return

    for i in range(N):
        cols[cur] = i
        if check(cur):
            recur(cur+1)
recur(0)
print(res)