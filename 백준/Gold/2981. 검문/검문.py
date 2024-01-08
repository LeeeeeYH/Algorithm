import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

N = int(input())
inputls = [int(input()) for _ in range(N)]
ls = [abs(inputls[i] - inputls[i-1]) for i in range(N)]

allgcd = gcd(ls[0], ls[1])
for i in range(2, N):
    allgcd = gcd(allgcd, ls[i])

for i in range(2, allgcd+1):
    if allgcd % i == 0:
        print(i, end=" ")