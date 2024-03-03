input = __import__('sys').stdin.readline

L, P = map(int, input().split())
peo = L*P
print(*[x-peo for x in list(map(int, input().split()))])