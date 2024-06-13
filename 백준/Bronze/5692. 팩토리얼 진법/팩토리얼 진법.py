input = __import__('sys').stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    i, multi, res = 1, 1, 0
    while N:
        res += N%10 * multi
        i, multi, N = i+1, multi*(i+1), N//10
    print(res)