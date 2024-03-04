input = __import__('sys').stdin.readline

dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
foods = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

for _ in range(K):
    newfoods = [[0]*N for _ in range(N)]
    # spring
    for x in range(N):
        for y in range(N):
            if trees[x][y]:
                trees[x][y].sort()
                leng = len(trees[x][y])
                for z in range(leng):
                    if foods[x][y] >= trees[x][y][z]:
                        foods[x][y] -= trees[x][y][z]
                        trees[x][y][z] += 1
                    else:
                        for tree in trees[x][y][z:leng]:
                            newfoods[x][y] += tree // 2
                        trees[x][y] = trees[x][y][:z]
                        break

    # summer
    for x in range(N):
        for y in range(N):
            foods[x][y] += newfoods[x][y]

    # fall
    for x in range(N):
        for y in range(N):
            if trees[x][y]:
                for z in trees[x][y]:
                    if z % 5 == 0:
                        for d in dirs:
                            dx, dy = x+d[0], y+d[1]
                            if 0 <= dx < N and 0 <= dy < N:
                                trees[dx][dy].append(1)

    # winter
    for x in range(N):
        for y in range(N):
            foods[x][y] += A[x][y]

res = 0
for x in range(N):
    for y in range(N):
        res += len(trees[x][y])
print(res)