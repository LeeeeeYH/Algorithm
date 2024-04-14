N = int(__import__('sys').stdin.readline())
for i in range(2*N-1):
    print('*'*(N-abs(i-N+1)), end='')
    print(' '*(2*abs(i-N+1)), end='')
    print('*'*(N-abs(i-N+1)))