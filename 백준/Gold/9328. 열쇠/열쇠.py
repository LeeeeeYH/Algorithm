import sys
input = sys.stdin.readline

dir = [[0,-1],[1,0],[0,1],[-1,0]]
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    board = [["*"]*(M+2)] + [['*']+list(input().rstrip())+['*'] for _ in range(N)] + [["*"]*(M+2)]
    check = [[False]*(M+2) for _ in range(N+2)]
    keys = [False]*26
    doors = [[] for _ in range(26)]
    # 열쇠 저장
    keyinput = input().rstrip()
    if keyinput != '0':
        for k in keyinput:
            keys[ord(k)-97] = True
    q = []
    res = 0

    def check_start(x, y):
        if not check[x][y]:
            global q, res
            start = board[x][y]
            if start == '.':
                q.append([x, y])
                check[x][y] = True
            elif start.islower():  # 키를 얻었다
                starti = ord(start) - 97
                q.append([x, y])
                check[x][y] = True
                if not keys[starti]:  # 키가 없었다면
                    keys[starti] = True  # 소지품 추가
                    if len(doors[starti]):  # 만난 문이 있다면 이제는 갈 수 있다.
                        for tx, ty in doors[starti]:
                            q.append([tx, ty])
                            check[tx][ty] = True
            elif start.isupper():  # 문을 만났다
                starti = ord(start) - 65
                if keys[starti]:  # 키가 있으면? 따고 들어가자
                    q.append([x, y])
                    check[x][y] = True
                else:  # 키가 없으면? 키찾을때까지 보류
                    doors[starti].append([x, y])  # 만난 문 목록에 추가
            elif start == '$':
                res += 1
                q.append([x, y])
                check[x][y] = True

    # 입구 찾기
    for i in range(1, N+1):
        check_start(i, 1)
        check_start(i, M)
    for j in range(2, M):
        check_start(1, j)
        check_start(N, j)

    while q:
        x, y = q.pop(0)
        for d in dir:
            dx, dy = x+d[0], y+d[1]
            cur = board[dx][dy]
            if not check[dx][dy]:
                if cur == '.':
                    q.append([dx, dy])
                    check[dx][dy] = True
                elif cur.islower():  # 키를 얻었다
                    curi = ord(cur)-97
                    q.append([dx, dy])
                    check[dx][dy] = True
                    if not keys[curi]:  # 키가 없었다면
                        keys[curi] = True  # 소지품 추가

                        if len(doors[curi]):  # 만난 문이 있다면 이제는 갈 수 있다.
                            for tx, ty in doors[curi]:
                                q.append([tx, ty])
                                check[tx][ty] = True

                elif cur.isupper():  # 문을 만났다
                    curi = ord(cur)-65
                    if keys[curi]:  # 키가 있으면? 따고 들어가자
                        q.append([dx, dy])
                        check[dx][dy] = True
                    else:  # 키가 없으면? 키찾을때까지 보류
                        doors[curi].append([dx, dy])  # 만난 문 목록에 추가
                elif cur == '$':
                    res += 1
                    q.append([dx, dy])
                    check[dx][dy] = True

    print(res)