input = __import__('sys').stdin.readline

K, N, M = map(int, input().split())
print(max(0, K*N-M))