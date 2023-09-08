import sys
input = sys.stdin.readline

D, K = map(int, input().split())

def recur(cur, a, b): # param: b의 idx, cur-1값 , cur 값
    if cur == 2:
        print(a)
        print(b)
        exit(0)

    if 1 <= b-a <= a:
        recur(cur-1, b-a, a)

for i in range(K-1, 0, -1):
    recur(D, i, K)