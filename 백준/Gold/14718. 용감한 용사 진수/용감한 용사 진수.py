import sys
input = sys.stdin.readline

N, K = map(int, input().split())
soldiers = [list(map(int, input().split())) for _ in range(N)]
res = 3_000_000
for i in range(N):
    for j in range(N):
        for k in range(N):
            # 힘은 i번째, 민첩은 j번째, 지능은 k번째 병사인 것들만 탐색
            stro, dex, inte = soldiers[i][0], soldiers[j][1], soldiers[k][2]
            cnt = 0
            for soldier in soldiers:
                if soldier[0] <= stro and soldier[1] <= dex and soldier[2] <= inte:
                    cnt += 1
            if cnt >= K:
                res = min(res, stro+dex+inte)

print(res)