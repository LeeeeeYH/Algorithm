from collections import deque
input = __import__('sys').stdin.readline

N, K = map(int, input().split())
MAX = 100_000
check = [False]*(MAX+1)
q = deque()
q.append([N, 0])
check[N] = True
while q:
    cur, cnt = q.popleft()
    if cur == K:
        print(cnt)
        break

    if cur*2 <= MAX and not check[cur*2]:
        check[cur*2] = True
        q.appendleft([cur*2, cnt])
    if cur > 0 and not check[cur-1]:
        check[cur-1] = True
        q.append([cur-1, cnt+1])
    if cur < MAX and not check[cur+1]:
        check[cur+1] = True
        q.append([cur+1, cnt+1])