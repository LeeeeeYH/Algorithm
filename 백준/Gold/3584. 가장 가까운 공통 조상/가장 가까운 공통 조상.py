input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    parent = [0]*(N+1)
    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A

    a, b = map(int, input().split())  # 가가공조 구할 노드
    pa = set()
    while a != 0:
        pa.add(a)
        a = parent[a]

    while True:
        if b in pa:
            print(b)
            break
        b = parent[b]