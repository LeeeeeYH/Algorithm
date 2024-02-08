import sys
input = sys.stdin.readline

N = int(input())
m_ing = list(map(int, input().split()))
ls = [list(map(int, input().split())) for _ in range(N)]
res, res_selected = 7501, []

def recur(cur, ing, flag):
    if cur == N:
        for i in range(4):
            if m_ing[i] > ing[i]:
                break
        else:
            global res, res_selected
            if res > ing[4]:
                res = ing[4]
                res_selected = [[i+1 for i in range(N) if flag & 1<<i]]
            elif res == ing[4]:
                res_selected += [[i+1 for i in range(N) if flag & 1<<i]]
        return

    next_ing = [0]*5
    for i in range(5):
        next_ing[i] = ing[i] + ls[cur][i]
    recur(cur + 1, next_ing, flag | 1<<cur)
    recur(cur+1, ing, flag)

recur(0, [0]*5, 0)
if res == 7501:
    print(-1)
else:
    print(res)
    print(*sorted(res_selected)[0])