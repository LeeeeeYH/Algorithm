import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())
print((A*(10**N)//B)%10)