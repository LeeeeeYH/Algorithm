input = __import__('sys').stdin.readline
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(L - max((A-1)//C+1, (B-1)//D+1))