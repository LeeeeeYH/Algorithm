input = __import__('sys').stdin.readline

ls = [int(input()) for _ in range(7)]
summ, minn = 0, 100
for i in ls:
    if i%2 != 0:
        summ += i
        minn = min(minn, i)

if summ > 0:
    print(summ, minn, sep='\n')
else:
    print(-1)