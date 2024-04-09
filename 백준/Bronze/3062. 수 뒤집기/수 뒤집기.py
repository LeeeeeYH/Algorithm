for _ in range(int(__import__('sys').stdin.readline())):
    N = input().rstrip()
    summ = str(int(N[::-1]) + int(N))
    leng = len(summ)
    for i in range(leng//2):
        if summ[i] != summ[leng-i-1]:
            print('NO')
            break
    else:
        print('YES')