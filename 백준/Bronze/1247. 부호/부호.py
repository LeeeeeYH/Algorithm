import sys
input = sys.stdin.readline

for _ in range(3):
    S = sum([int(input()) for _ in range(int(input()))])
    if S > 0: print('+')
    elif S < 0: print('-')
    else: print('0')