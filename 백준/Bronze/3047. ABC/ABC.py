input = __import__('sys').stdin.readline

inp = sorted(map(int, input().split()))
s = input().rstrip()
ls = [0]*3
ls[str(s).index('A')] = inp[0]
ls[str(s).index('B')] = inp[1]
ls[str(s).index('C')] = inp[2]
print(*ls)