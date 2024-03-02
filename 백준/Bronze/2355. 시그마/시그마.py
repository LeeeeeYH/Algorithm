input = __import__('sys').stdin.readline

A, B = map(int, input().split())
print((A+B)*(abs(B-A)+1)//2)