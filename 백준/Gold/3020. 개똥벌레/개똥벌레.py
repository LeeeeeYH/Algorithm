import sys
input = sys.stdin.readline

N, H = map(int, input().split())
wall = [0]*(H+1)
wall[0] = N//2 # 1번째 높이의 장애물 수 == 석순 수 == N//2
for i in range(N):
    if i % 2 == 0: # 석순은 석순+1 높이부터 장애물이 없어짐
        wall[int(input()) + 1] -= 1
    else: # 종유석은 H - 종유석높이 + 1부터 장애물이 생김
        wall[H - int(input()) + 1] += 1

cur_wall = N//2
min_wall, min_wall_N = N//2, 1 # 장애물의 최솟값, 최솟값인 갯수, 초기화는 석순개수(높이 1)

for i in range(2, H+1):
    cur_wall += wall[i]
    if min_wall > cur_wall:
        min_wall = cur_wall
        min_wall_N = 1
    elif min_wall == cur_wall:
        min_wall_N += 1

print(min_wall, min_wall_N)