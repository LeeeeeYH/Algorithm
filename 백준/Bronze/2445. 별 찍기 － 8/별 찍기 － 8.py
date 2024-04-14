N = int(__import__('sys').stdin.readline())
for i in range(2*N-1):
    print('*'*(N-abs(i-N+1)), ' '*(2*abs(i-N+1)), '*'*(N-abs(i-N+1)), sep='')
