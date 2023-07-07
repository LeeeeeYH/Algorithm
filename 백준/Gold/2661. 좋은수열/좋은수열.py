import sys
input = sys.stdin.readline

N = int(input())

def check(num):
    for i in range(1, len(num)//2+1):
        if num[-i:] == num[-i-i:-i]:
            return False
    return True

def recur(cur, num):
    if cur == N:
        print(num)
        exit(0)

    for i in range(1, 4):
        nnum = num+str(i)
        if check(nnum):
            recur(cur+1, nnum)

recur(0, '')