input = __import__('sys').stdin.readline

N = int(input())
ls = [input().rstrip() for _ in range(N)]
leng = len(ls[0])

for i in range(1, leng+1):
    if N == len(set([num[leng - i:] for num in ls])):
        print(i)
        exit(0)