import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
leng = 2*n
selected = [0]*n
res = 0

# 조합 뽑기
def recur(cur, start):
    if cur == n:
        global res
        clear = 0
        for quest in ls:
            for skill in quest:
                if skill not in selected:
                    break
            else:
                clear += 1

        res = max(res, clear)
        return

    for i in range(start, leng + 1):
        selected[cur] = i
        recur(cur + 1, i + 1)

recur(0, 1)
print(res)