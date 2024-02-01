import sys
input = sys.stdin.readline

N = int(input())
ls = [0]*N

def check(leng):
    for i in range(1, leng//2+1):
        if ls[leng-i:leng] == ls[leng-i-i:leng-i]:
            return False
    return True

def recur(cur):
    if cur == N:
        print(*ls, sep="")
        exit(0)

    for i in range(1, 4):
        ls[cur] = i
        if check(cur+1):
            recur(cur+1)
recur(0)