import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ls = [0 if i%2==0 else 1 for i in list(map(int, input().split()))]

i = 0
res = 0
summ = 0

for j in range(N):
    if ls[j]:  # 홀수 일때
        if K > summ:  # 삭제할 기회가 남아있으면
            summ += 1  # 삭제하고
        else:
            while ls[i] == 0:
                i += 1
            i += 1
    res = max(res, j - i + 1 - summ)
print(res)