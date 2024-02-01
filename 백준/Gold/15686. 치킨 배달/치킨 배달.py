import sys
input = sys.stdin.readline

N, M = map(int, input().split())
houses, chickens = [], []
res = 1300

# 집과 치킨집 각각의 좌표를 list 저장
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            houses.append([i, j])
        elif row[j] == 2:
            chickens.append([i, j])


# 맨해튼 거리
def dis(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# 각 집에대해서 치킨집까지의 거리, 행: 집, 열: 치킨집
distances = [[dis(chicken, house) for chicken in chickens] for house in houses]

# check(살아남은 치킨집 bit)에 대해 가까운 치킨집 거리 더하기
def sum_min_dis(check):
    ret = 0
    for i in range(len(houses)): # 집마다
        mindis = 100
        for j in range(len(chickens)): # 치킨집마다
            if check & 1<<j: # 살아남은 치킨집이면
                mindis = min(mindis, distances[i][j]) # 젤 가까운 치킨집 구하기
        ret += mindis
    return ret

# 조합으로 구함
def recur(cur, start, check):
    global res
    if cur == M: # M개 치킨집 다 뽑았다
        res = min(res, sum_min_dis(check))
        return

    for i in range(start, len(chickens)):
        if not check & 1<<i:
            recur(cur+1, i+1, check|1<<i)

recur(0,0,0)
print(res)