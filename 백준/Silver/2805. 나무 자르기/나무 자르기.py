import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def cut(hei):
    s = 0
    for t in trees:
        s += max(0, t-hei)
    return s

i, j = 0, max(trees)
res = 0
while i <= j:
    mid = (i+j)//2
    if cut(mid) >= M:
        res = mid
        i = mid + 1
    else:
        j = mid - 1
        
print(res)