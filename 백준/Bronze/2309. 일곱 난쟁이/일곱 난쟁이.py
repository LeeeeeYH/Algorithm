import sys
input = sys.stdin.readline

ls = sorted([int(input()) for _ in range(9)])
summ = sum(ls) - 100
i, j = 0, 8
while i < j:
    if ls[i] + ls[j] < summ:
        i += 1
    elif ls[i] + ls[j] > summ:
        j -= 1
    else:
        print(*(ls[:i]+ls[i+1:j]+ls[j+1:]), sep="\n")
        exit(0)