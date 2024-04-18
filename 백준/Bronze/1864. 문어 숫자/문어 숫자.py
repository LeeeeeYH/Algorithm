input = __import__('sys').stdin.readline

nums = ['-','\\','(','@','?','>','&','%','/']
while True:
    S = input().rstrip()
    if S == '#':
        break

    eight, res = 1, 0
    for i in S[::-1]:
        num = nums.index(i)
        if num == 8:
            res += -eight
        else:
            res += eight*num
        eight *= 8
    print(res)