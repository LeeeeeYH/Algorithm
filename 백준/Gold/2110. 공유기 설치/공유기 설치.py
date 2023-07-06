import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])

i, j = 1, 1_000_000_000
res = 0
while i <= j:
    mid = (i+j)//2
    cnt = 1 # 공유기 설치할 집 수
    left = houses[0] # 계속 움직이며 거리 계산할 왼쪽 집
    for house in houses[1:]:
        if house - left >= mid: # (설치할-이전설치한)집 거리가 mid보다 크면
            cnt += 1
            left = house
    if cnt >= C: # 설치 가능
        res = mid
        i = mid + 1
    else:
        j = mid - 1

print(res)