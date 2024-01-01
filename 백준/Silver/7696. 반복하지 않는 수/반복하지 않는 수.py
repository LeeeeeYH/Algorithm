import sys
input = sys.stdin.readline

ls = []

def recur(num, leng, flag):
    if leng >= 9:
        return

    ls.append(num)
    for i in range(10):
        if not flag & 1<<i:
            recur(num * 10 + i, leng + 1, flag | 1 << i)

for i in range(1, 10):
    recur(i, 1, 1<<i)
ls.sort()

while True:
    tc = int(input())
    if tc == 0:
        break
    print(ls[tc-1])
