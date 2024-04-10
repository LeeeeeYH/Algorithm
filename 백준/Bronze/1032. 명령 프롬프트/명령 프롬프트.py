input = __import__('sys').stdin.readline

N = int(input())
s = input().rstrip()
leng = len(s)
check = [True]*leng
for _ in range(N-1):
    ss = input().rstrip()
    for i in range(leng):
        if ss[i] != s[i]:
            check[i] = False

for i in range(leng):
    print(s[i] if check[i] else '?', end='')