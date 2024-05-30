input = __import__('sys').stdin.readline

num = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break

    if n0 % 2 == 0:
        print(num, ". even ", n0//2, sep='')
    else:
        print(num, ". odd ", (n0-1)//2, sep='')
    num += 1