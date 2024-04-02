input = __import__('sys').stdin.readline

dirs = [[0,-1],[1,0],[0,1],[-1,0]]
sand_ratio = [[-1,  1, 0.01],
              [-1, -1, 0.01],
              [ 0,  2, 0.02],
              [ 0,  1, 0.07],
              [ 0, -1, 0.07],
              [ 0, -2, 0.02],
              [ 1,  1,  0.1],
              [ 1, -1,  0.1],
              [ 2,  0, 0.05]]
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
distances = [i // 2 + 1 for i in range((N - 1) * 2)]
distances.append(distances[-1])
x, y, d = N//2, N//2, 0
res = 0  # 격자 밖으로 날아간 모래양

# 토네이도의 이동
for dis in distances:
    for _ in range(dis):
        x, y = x + dirs[d][0], y + dirs[d][1]  # 이동 하고

        all = alpha = A[x][y]
        for s, l, ratio in sand_ratio:  # d방향만큼, 반시계 90도 회전한 만큼, 비율
            dd = (d+1)%4
            dx, dy, sand = x + dirs[d][0]*s + dirs[dd][0]*l, y + dirs[d][1]*s + dirs[dd][1]*l, int(all*ratio)
            alpha -= sand
            if 0 <= dx < N and 0 <= dy < N:
                A[dx][dy] += sand
            else:
                res += sand

        # 알파 위치 계산
        dx, dy = x + dirs[d][0], y + dirs[d][1]
        if 0 <= dx < N and 0 <= dy < N:
            A[dx][dy] += alpha
        else:
            res += alpha

        # y위치 모래 0처리
        A[x][y] = 0

    d = (d+1) % 4

print(res)