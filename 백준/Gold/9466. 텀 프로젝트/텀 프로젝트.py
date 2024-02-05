from sys import stdin
input = stdin.readline

T = int(input())
res = ''
for _ in range(T):
    n = int(input())
    ls = [0] + list(map(int, input().split()))
    visited = [False]*(n+1)  # 방문 확인
    res = n

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            if ls[i] == i:  # 자기 자신을 원하면
                res -= 1
                continue

            team = [i]
            cur = i
            while True:  # 원하는 사람 찾아 계속 탐색
                cur = ls[cur]
                if visited[cur]:
                    if cur in team:
                        res -= len(team) - team.index(cur)
                    break

                visited[cur] = True
                team.append(cur)
    print(res)