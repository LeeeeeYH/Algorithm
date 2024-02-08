import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = []
for _ in range(N):
    guitar, song = input().split()
    ls.append([1 if song[i]=='Y' else 0 for i in range(M)])

maxsong = 0
res = 0

def recur(cur, guitars, play):
    if cur == N:
        global maxsong, res
        summ = sum(play)
        if maxsong < summ:
            maxsong = summ
            res = guitars
        elif maxsong == summ:
            res = min(res, guitars)
        return

    # 선택 안하고
    recur(cur+1, guitars, play)
    # 선택 하고
    next_play = [0]*M
    for i in range(M):
        next_play[i] = play[i] | ls[cur][i]
    recur(cur+1, guitars+1, next_play)

recur(0, 0, [0]*M)
print(res if maxsong != 0 else -1)