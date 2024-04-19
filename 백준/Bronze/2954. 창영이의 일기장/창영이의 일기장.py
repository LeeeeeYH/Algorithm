input = __import__('sys').stdin.readline

mo = {'a', 'e', 'i', 'o', 'u'}
S = input().rstrip()
leng = len(S)
i = 0
while i < leng:
    print(S[i], end='')
    if S[i] in mo:
        i += 2
    i += 1