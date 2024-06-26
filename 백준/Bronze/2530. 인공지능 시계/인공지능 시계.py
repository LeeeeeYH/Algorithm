input = __import__('sys').stdin.readline

A,B,C = map(int, input().split())
D = int(input())
time = (A*3600+B*60+C+D)%(3600*24)
print(time//3600, time%3600//60, time%60)