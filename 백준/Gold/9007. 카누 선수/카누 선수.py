import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    ls = [sorted(map(int, input().split())) for _ in range(4)]

    A, B = [], []
    for i in range(n):
        for j in range(n):
            A.append(ls[0][i]+ls[1][j])
            B.append(ls[2][i]+ls[3][j])

    A.sort()
    B.sort()

    leng = len(A)
    j = len(B)-1
    res, resdis = 0, 40_000_000
    for i in range(leng):
        while j >= 0:
            summ = A[i] + B[j]
            dis = abs(k - summ)
            if resdis > dis:
                res, resdis = summ, dis
            elif resdis == dis and res > summ:
                res = summ

            if k < summ:
                j -= 1
            else:
                break

    print(res)