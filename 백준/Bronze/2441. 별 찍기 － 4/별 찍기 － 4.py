input = __import__('sys').stdin.readline

N = int(input())
for i in range(N):
    print(' '*i + '*'*(N-i))