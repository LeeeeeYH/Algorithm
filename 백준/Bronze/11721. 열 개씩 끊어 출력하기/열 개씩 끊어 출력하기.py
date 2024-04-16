input = __import__('sys').stdin.readline

S = input().rstrip()
for i in range(len(S)):
    print(S[i], end='')
    if i % 10 == 9:
        print()