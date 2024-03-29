N = int(__import__('sys').stdin.readline())
for i in range(N, 0, -1):
    print(' '*(N-i) + '*'*(2*i-1))