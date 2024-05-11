input = __import__('sys').stdin.readline

N = int(input())
for i in range(2*N-1):
    print(' '*abs(i-N+1), '*'*(N - abs(i-N+1)),sep='')