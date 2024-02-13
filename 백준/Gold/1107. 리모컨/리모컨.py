import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
ls = []
if M > 0:
    ls = list(map(int, input().split()))
buttons = [i for i in range(10) if i not in ls]
res = abs(N-100)

def recur(cur, count):
    disN = abs(cur - N)  # N까지 위아래만 눌러서 갈 때의 거리
    global res
    res = min(res, disN + count)  # 여태 누른 번호 + 위아래로 가는 거리

    # 고장 안난 번호 또 누르기
    for i in buttons:
        next = cur*10 + i
        if abs(next - N) < disN:  # 더 적을때만 진행
            recur(next, count+1)

for i in buttons:
    recur(i, 1)
print(res)