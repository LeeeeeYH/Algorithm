import sys
input = sys.stdin.readline

N, S = map(int, input().split())
ls = list(map(int, input().split()))
mid = N//2

ldict, rdict = dict(), dict()
def lrecur(cur, summ):
    if cur == mid:
        if summ in ldict:
            ldict[summ] += 1
        else:
            ldict[summ] = 1
        return

    lrecur(cur+1, summ+ls[cur])
    lrecur(cur+1, summ)

def rrecur(cur, summ):
    if cur == N:
        if summ in rdict:
            rdict[summ] += 1
        else:
            rdict[summ] = 1
        return

    rrecur(cur + 1, summ + ls[cur])
    rrecur(cur + 1, summ)

lrecur(0, 0)
rrecur(mid, 0)

res = 0
for i in ldict.keys():
    if S - i in rdict.keys():
        res += ldict[i] * rdict[S - i]

print(res if S != 0 else res-1)